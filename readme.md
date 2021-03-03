# Implementacion de One Time Pad

Este proyecto esta utilizando un virtual enviroment de python. Para activarlo se corre el siguiente comando:
###Windows
``.\env\Scripts\activate``

### MacOS
``source env/bin/activate``

## Para encriptar
``python encrypt.py``
<br/>
Al terminar de correr el programa se generan dos archivos:
- ``me.txt`` : Este es el mensaje encriptado
- ``otp.txt`` : Este es el One Time Pad (llave)

## Para desencriptar
``python decrypt [nombre de archivo de mensaje].txt [nombre de archivo de One Time Pad].txt``