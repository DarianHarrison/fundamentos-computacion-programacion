# Clasificacion de artículos periodísticos

## 0.Prerequisitos 

a) descargar dataset de este proyecto y guardar como articulos.csv
```
articulos.csv
```

b) instalar librerías/paquetes de python

desde una terminal
```
pip install pandas
pip install numpy
pip install sklearn
```

## 1.Análisis de datos

a) abrir una hoja de python "ejemplo.py" y pegar el siguiente código para importar dependencias
```
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
```

b) leer el datastet 
```
data = pd.read_csv("articles.csv", sep='\t')
print(data.head())
```

c) analizar datos

contiente nulos ?
```
print(data.isnull().sum())
```

d) cuántos artículos de cada categoría ?
```
print(data["category"].value_counts())
```

## 2. Entrenamiento

a) preparar datos / convertir datos a vectores
```
data = data[["title", "category"]]

x = np.array(data["title"])
y = np.array(data["category"])

cv = CountVectorizer()
X = cv.fit_transform(x)
```

b) separar datos en train y test
```
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

c) Utilizar algoritmo para entrenar/aprender un modelo
```
model = MultinomialNB()
model.fit(X_train,y_train)
```

## 3. Predicción

a) escribir algún título de noticia a predecir
```
predict_input="Latest Apple iPhone SE 3 concept renders show a compact smartphone in the style of the iPhone 4"
```

b) preprocesar texto similar al primer paso de entrenamiento "3.a)" para poder comparar manzanas con manzanas
```
data = cv.transform([user]).toarray()
```

c) ahora si utilizar el modelo entrenado apra predecir
```
output = model.predict(data)
print(output)
```










# Bibliografía
```
fuente: https://thecleverprogrammer.com/2021/10/07/news-classification-with-machine-learning/
```