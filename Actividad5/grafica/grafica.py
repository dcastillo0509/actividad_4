import matplotlib.pyplot as plt
#Importa la librería matplot como plt para graficar
import numpy as np
#importa la librería numpy como np



def gr_con_prediccion(x_lim,y_lim):
  #Define la función con variables de entrada
  plt.figure(figsize=(15, 6))
  #con matplot establece el tamaño de la gráfica
  plt.plot(data.data_teorico['Esfuerzo[kN]'] , data.data_teorico['Deformacion[mm]'])
  #Grafica esfuerzo,deformación teóricos
  plt.scatter(	data_real['Esfuerzo[kN]'] , data_real['Deformacion[mm]'], color='red')
  #Grafica esfuerzo,deformación reales en color rojo
  plt.xlabel('Esfuerzo [kN]')
  #Asigna etiqueta del eje x
  plt.ylabel('Deformación [mm]')
  #Asigna etiqueta del eje y
  plt.title('Gráfica 2: teórico versus real [ZOOM]')
  #Asigna el título de la gráfica
  plt.xlim(0, x_lim)
  #Establece el límite en el eje x de 0 a x_lim
  plt.ylim(0, y_lim)
  #Establece el límite en el eje y de 0 a y_lim
  plt.grid()
  #Genera una grilla a la gráfica
  plt.gca().invert_yaxis()
  #Invierte los ejes

def gr_con_prediccion_3000(prediction):
  #Define la función con variables de entrada
  plt.figure(figsize=(15, 6))
  #con matplot establece el tamaño de la gráfica
  plt.plot(	data_teorico['Esfuerzo[kN]'] , data_teorico['Deformacion[mm]'])
  #Grafica esfuerzo,deformación teóricos
  plt.scatter(data.data_real['Esfuerzo[kN]'] , data.data_real['Deformacion[mm]'], color='red')
  #Grafica esfuerzo,deformación reales en color rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
  #en valores equidistantes de 0 a 1000 se hace la predicción y se grafica en color magenta
  plt.scatter(	3000 , prediction, color='green')
  #Dibuja un punto verde en el esfuerzo 3000 y la predicción de la deformación para este valor
  plt.xlabel('Esfuerzo [kN]')
  #Asigna etiqueta del eje x
  plt.ylabel('Deformación [mm]')
  #Asigna etiqueta del eje x
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN')
  #Asigna etiqueta del eje x
  plt.xlim(0, 3000)
  #Establece el límite en el eje x de 0 a 3000
  plt.ylim(0, 45)
  #Establece el límite en el eje y de 0 a 45
  plt.grid()
  #Genera una grilla a la gráfica
  plt.gca().invert_yaxis()
  #Invierte los ejes

def gr_sin_prediccion():
  #Define la función sin variables de entrada
  plt.figure(figsize=(15, 6))
  #con matplot establece el tamaño de la gráfica
  plt.plot(	data_teorico['Esfuerzo[kN]'] , data_teorico['Deformacion[mm]'])
  #Grafica esfuerzo,deformación teóricos
  plt.scatter(	data_real['Esfuerzo[kN]'] , data_real['Deformacion[mm]'], color='red')
  #Grafica esfuerzo,deformación reales en color rojo
  plt.xlabel('Esfuerzo [kN]')
  #Asigna etiqueta del eje x
  plt.ylabel('Deformación [mm]')
  #Asigna etiqueta del eje x
  plt.title('Gráfica 1: teórico versus real')
  #Asigna etiqueta del eje x
  plt.grid()
  #Genera una grilla a la gráfica
  plt.gca().invert_yaxis()
  #Invierte los ejes