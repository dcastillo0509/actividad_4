from data.data import *
#desde la carpeta data se extrae todo el archivo data
from BD.baseDatos import *
#desde la carpeta DB se extrae todo el archivo baseDatos
from sklearn.linear_model import LinearRegression
from grafica.grafica import *
#desde la carpeta grafica se extrae todo el archivo grafica
import pandas as pd
#Se importa la librería pandas como pd



#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()
#Los datos de esfuerzo,deformación se asignan ejecutando la función dataTeorico()

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos()
#Se crea la variable data_list y se asigna el resultado de la ejecución de la función lecturaDatos
deformacion_3 = pd.DataFrame(data_list)
#Se crea la variable deformacion_3 y se crea un dataframe del data_list usando pandas
deformacion_3_fit = deformacion_3 #Se crea la variable deformacion_3_fit y se asigna el dataframe de deformacion_3
X = deformacion_3_fit['Esfuerzo[kN]'].values.reshape(-1, 1)
#se define la variable x y se asignan los valores de esfuerzos en una sola columna
y = deformacion_3_fit['Deformacion[mm]'].values.reshape(-1, 1)
#se define la variable x y se asignan los valores de deformacion en una sola columna
x_lim = deformacion_3['Esfuerzo[kN]'].iloc[-1]
#crea una variable x_lim y aasigna el último valor de esfuerzo
y_lim = deformacion_3['Deformacion[mm]'].iloc[-1]
#crea una variable y_lim y aasigna el último valor de deformacion
model = LinearRegression()
#crea la variable regresion y ejecuta la funcion de regresion lineal de una biblioteca
model.fit(X, y)
#ajusta el modelo de regresión con dato de entrada x, salida y
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)
#se crea la variable prediction, el resultado se redondea a 1 decimal.
#Con el modelo se realiza una predicción para un valor de 3000
print('la predicción a 3000 kN es de: ', prediction ,'mm')
#Se imprime un mensaje con el resultado de la predicción

dataRealEsfuerzo = deformacion_3['Esfuerzo[kN]']
#Se crea una variable que contanga los datos de los esfuerzos
dataRealDeformacion = deformacion_3['Deformacion[mm]']
#Se crea una variable que contenga los datos de las deformaciones

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
#Ejecuta la función gr_sin_prediccion de gráfica
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
#Ejecuta la función gr_con_prediccion de gráfica
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)
#Ejecuta la función gr_con_prediccion_3000 de gráfica
