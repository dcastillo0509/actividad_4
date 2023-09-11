import pandas as pd #importa pandas como pd

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\David\Desktop\Actividad5\data\Data ingeniero.csv")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #se define la función dataTeorico
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]']
    #Se crea la variable dataTeoricoEsfuerzo y se asignan los datos de los esfuerzos
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']
    #Se crea la variable dataTeoricoDeformacion y se asignan los datos de las deformaciones
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion
    #retorna los datos de esfuerzo,deformacion