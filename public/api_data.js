define({ "api": [
  {
    "type": "post",
    "url": "/predict",
    "title": "Predecir la raza del perro en la imagen",
    "name": "GetPrediction",
    "group": "Endpoints",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "raza",
            "description": "<p>Raza del Perro.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./server.py",
    "groupTitle": "Endpoints"
  }
] });
