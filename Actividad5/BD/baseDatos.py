#Se debe instalar pymongo desde la terminal
#pip install pymongo

from pymongo.mongo_client import MongoClient
#Desde la carpeta pymongo se importa mongo_client y se nombra

def conexion(): #se define la funcion conexion
    uri = "mongodb+srv://davidmateo0509:1234@cluster0.afpjypb.mongodb.net/?retryWrites=true&w=majority"
    # Se crea la variable uri para la conexión al servidor de mongo
    return MongoClient(uri)
    #se retorna la conexión a MongoClient con los datos de uri

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():#Se define la función lecturaDatos
    client = conexion()#Se define una variable client y almacena los datos al ejecutar la conexión
    db = client.Cluster0.deformaciones.deformacion_3
    #se crea la variable db y se asignan los datos de deformacion_3 que se encuentra en la ruta client/actividad4/deformaciones
    data_list = []#Se crea una lista data_list en blanco
    for deformacion_3 in db.find():
    #se inicia ciclo for en data_real_bd y se buscan todos los datos de db
        data_list.append(deformacion_3)
        #a la lista data_list se le agregan los datos de data_real_db 
    return data_list #Retorna data_list

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""