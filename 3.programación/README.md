# Pasos para instlar NodeJS y Python

## 1. Sistema operativo Windows

a) NodeJS

instalación y comprobación
```
https://www.youtube.com/watch?v=BgtB31gXkoA
```

b) Python 3

instalación y comprobación
```
https://www.youtube.com/watch?v=9fNKy9zOPkg
```


## 2. Sistema operativo Linux (asumiento sistema ubuntu 20.04)

a) NodeJS

instalación
```bash
sudo apt install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -ys nodejs
```
comprobación
```bash
node --version
npm --version
````
v14.18.1
8.1.1


b) Python 3
instalación
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```
comprobación
```bash
python3 --version
pip3 --version
````
Python 3.8.10
pip 21.3


## 3. Ejemplo de codificacion base64 y ascii

a) CODIFICAR
a.1) jpg a base64 (utilizado para transportar imagenes y otros datos en internet)
```
https://base64.guru/converter/encode/image/jpg
```
a.2) obtener los datos binarios de la codificacion base64 a la codificacion binaria (1/0, pulsos de luz, corriente/no-correinte, predido/apagado, etc..)

```
https://onlineutf8tools.com/convert-utf8-to-binary
```

b) DECODIFICAR
una vez nuestros datos hayan llegado a su destino hay que decodificarlos e interpretarlos
b.1) binaro a base64
```
https://onlineutf8tools.com/convert-binary-to-utf8
```
b.2) base64 a jpeg
```
https://base64.guru/converter/decode/image/jpg
```