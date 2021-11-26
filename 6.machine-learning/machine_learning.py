import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

## 1.Análisis de datos ##
#########################

# leer el datastet
data = pd.read_csv("articles.csv", sep='\t')

# imprimir primeros 5 registros
print(data.head())

# hay nulos ?
print(data.isnull().sum())

# contar numero de titulos por categoria
print(data["category"].value_counts())


## 2. Entrenamiento ##
######################

# preprocesar, convertir texto a vectores

data = data[["title", "category"]]

x = np.array(data["title"])
y = np.array(data["category"])

cv = CountVectorizer()
X = cv.fit_transform(x)

data = data[["title", "category"]]

x = np.array(data["title"])
y = np.array(data["category"])

cv = CountVectorizer()
X = cv.fit_transform(x)


# dividir datos 80% para entrenamiento y 20% para testeo

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# declarar modelo de entrenamiento con algoritmo MultinomialNB
model = MultinomialNB()

# Entrenar modelo
model.fit(X_train,y_train)


## 3. Predicción #####
######################

# escribir algún título de un texto
predict_input="Dow futures plunge 700 points amid fears of new Covid variant in South Africa"

# preprocesar, convertir texto a vectores
data = cv.transform([predict_input]).toarray()

# utilizar modelo para predecir categoria de título
output = model.predict(data)
print(output)