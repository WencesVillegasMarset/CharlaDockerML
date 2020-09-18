# Charla Docker + ML
Charla Docker + ML @ Meetup Ciencia de Datos Mendoza

Colab Notebook https://colab.research.google.com/drive/1KrcFMyWb8ttF3PqEv07BYXPNV9YShR6r#scrollTo=KP_fwPayl_iD


Para correr la imagen docker desde el container registry:


```console
bash:~$ docker run --detach --publish 5000:5000 --name wences-dog-classifier wencesvillegas/dogbreedml:1.7 
```
(Luego descargarse puede tardar unos segundos inicializando el modelo)


