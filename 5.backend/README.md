# Práctica 5: Pasos para crear un backend en NodeJS

## 0. Prerequisitos

a) Haber instalado NodeJS (instrucciones al final de módulo 3)
b) Tener conexión al internet (para descargar software de forma programática)

## 1. Servidor REST API en NodeJS en Sistema operativo Linux y Windows

desde tu terminal
a) Crear un nuevo proyecto de NodeJS 
```bash
mkdir mi-servidor-restapi # crear un nuevo directorio
cd mi-servidor-restapi # navegar hacia el directorio
npm init # inicializar proyecto
```
nota: puedes aceptar los valores por default al dar "enter" a todo
```
package name: (mi-servidor-restapi) 
version: (1.0.0) 
description: 
entry point: (index.js) 
test command: 
git repository: 
keywords: 
author: 
license: (ISC) 
About to write to /home/darian/Desktop/mi-servidor-restapi/package.json:

{
  "name": "mi-servidor-restapi",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}


Is this OK? (yes) 
```

b) instalar packete exress

primero navegar a la carpeta proyecto
```bash
cd mi-servidor-restapi # navegar a directorio de nuestro proyecto
npm install express # instalar librería de express 
```

c) comprobar que la dependencia externa "express" aparece en nuestro archivo de package.json

contenido de package.json
```
{
  "name": "mi-servidor-restapi",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

d) crear un archivo de entrada a nuestro servidor llamado "index.js" que contenga las siguientes líneas de código
```
const express = require('express')
const app = express()
app.get('/', function (req, res) {
  res.send('Hello World')
})
app.listen(3000)
```


e) inicializemos el servidor

```
node index.js
```
Server running on port 3000


f) comprobar desde un navegador, navegar a localhost:3000 o bien 127.0.0.1:3000
```
http://127.0.0.1:3000
```


## Recursos
```
https://docs.npmjs.com/cli/v7/commands/npm-init/
https://www.npmjs.com/package/express
```

## Notas Adicionales

* Nota: En el presente ejercicio estamos creando un servidor http que está escuchando peticiones en el puerto 3000 de nuestra interfaz de red localhost
* Nota2: Localhost es un ambiente de desarrollo local equivalente a la ip 127.0.0.1 (en la práctica de la sesión 2 de redes descubrimos que tenemos esa interfaz de red). Local significa que aún no estamos saliendo al internet.
* Nota3: Salir a Internet tiene mayor grado de complejidades y debemos ser más cautelosos ya que nos abre la puerta a ciberataques, por lo que optamos por solamente utilizar la red local que es segura para desarrollo. 
* Nota4: La red local es lo que comunmente se utiliza para el ambiente de desarrollo inclusive en compañías grandes como google y facebook.
* Nota5: Los puertos para servidores http abiertos al internet, comunmente son 80 o 443
* El puerto 80 se utiliza para servidores web no seguros (http).
* El puerto 443 se utiliza para servidores web seguros (https).
