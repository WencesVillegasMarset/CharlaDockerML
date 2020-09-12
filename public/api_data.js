define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./public/main.js",
    "group": "C:\\Users\\wence\\Documents\\Documents\\repos\\CharlaDockerML\\public\\main.js",
    "groupTitle": "C:\\Users\\wence\\Documents\\Documents\\repos\\CharlaDockerML\\public\\main.js",
    "name": ""
  },
  {
    "type": "post",
    "url": "/predict",
    "title": "Predecir la raza del perro en la imagen",
    "name": "GetPrediction",
    "group": "Endpoints",
    "examples": [
      {
        "title": "Body",
        "content": "{\n\"image\": ImageFile.jpg\n}",
        "type": "body"
      }
    ],
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
