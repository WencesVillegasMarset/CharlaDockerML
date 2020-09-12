<a name="top"></a>
# De que raza es mi perro? - Wenceslao Villegas 42783 v1.0.0

Las razas soportadas son Border Collie, Doberman, Ovejero Aleman, Gran Danes, Pekines, Rhodesia, Husky SIberiano, Beagle, Collie y Schipekke!

- [Endpoints](#endpoints)
	- [Predecir la raza del perro en la imagen](#predecir-la-raza-del-perro-en-la-imagen)
	


# <a name='endpoints'></a> Endpoints

## <a name='predecir-la-raza-del-perro-en-la-imagen'></a> Predecir la raza del perro en la imagen
[Back to top](#top)



	POST /predict



### Examples

Body

```
{
"image": ImageFile.jpg
}
```



### Success 200

| Name     | Type       | Description                           |
|:---------|:-----------|:--------------------------------------|
|  raza | String | <p>Raza del Perro.</p>|

