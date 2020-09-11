
# Request ejemplo via CURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'


import keras.models
from PIL import Image
import numpy as np
import flask
import io
import tensorflow as tf


# inicializamos la app de Flask y la variable que ocontedra a nuestro modelo cargado
app = flask.Flask(__name__)
model = None

#aca cargamos el diccionario con las correspondencias de cada etiqueta 
class_dict = {0: 'Border_collie',
				1:'Doberman',
				2:'German_shepherd',
				3:'Great_Dane',
				4:'Pekinese',
				5:'Rhodesian_ridgeback',
				6:'Siberian_husky',
				7:'beagle',
				8:'collie',
				9:'schipperke'}
#esta funcion nos permite pasar de un arreglo de probabilidades a tener un diccionario con la etiquete de c/u y su probabilidad
#el segundo valor que devuelve es la clase en la que tiene mas confianza
def decode_predictions(prediction):
	result = dict(zip(class_dict.values(), prediction.tolist()[0]))
	confident_class = class_dict[np.where(prediction>0.5)[1][0]]
	return result, confident_class

def load_model():
	# cargamos el modelo de keras que tenemos en el repo poniendo su ruta como argumento en leado model
	#esto solo se ejecuta una vez ya que no necesitamos cargar el modelo con cada peticion
	global model
	model = keras.models.load_model('dog_classifier.h5')
	#guardamos el grafo por defecto de tensorflow por errores del backend, no se tendria que hacer en situaciones normales
	global graph
	graph = tf.get_default_graph()


def prepare_image(image, target_size):
	# si el modo de la imagen no es RGB la convertimos a ese tipo
	if image.mode != "RGB":
		image = image.convert("RGB")
	# ahora le hacemos el preprocessing necesario para que entre a la red.
	image = image.resize(target_size)
	image = keras.preprocessing.image.img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = image/255.0

	return image

@app.route('/<path:path>')
def api_index(path):
	return flask.send_from_directory('./public', path)

@app.route('/', methods=['GET'])
def index():
	return flask.send_from_directory('./public', "index.html")

"""
@api {post} /predict Predecir la raza del perro en la imagen
@apiName GetPrediction
@apiGroup Endpoints

@apiSuccess {String} raza Raza del Perro.
"""

@app.route("/predict", methods=["POST"])
def predict():
	# inicializamos el diccionario que va a devolver el metodo
	data = {"success": False}

	if flask.request.method == "POST":
		#nos aseguramos de que haya llegado la imagen por POST
		if flask.request.files.get("image"):
			# leemos la imagen y la transformamos a formato PIL
			image = flask.request.files["image"].read()
			image = Image.open(io.BytesIO(image))

			# preprocesamos la imagen
			image = prepare_image(image, target_size=(224, 224))

			# clasificamos la imagen
			with graph.as_default():
				preds = model.predict(image)
			
			# procesamos los resultados de predciccion para que sean legibles
			full_result, class_predicted = decode_predictions(preds)
			# armamos el diccionario que vamos a devolver al usuario
			data["predictions"] = class_predicted
			data['probabilities'] = full_result
			data["success"] = True

	# returnamos los resultados en formato json
	return flask.jsonify(data)

# cuando corramos python esta_script.py detecta que el hilo de ejecucion primario es este (main), carga el modelo y luego el server
if __name__ == "__main__":
	print("Cargando el modelo e iniciando el servidor Flask!")
	load_model()
	app.run(host='0.0.0.0')
