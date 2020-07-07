#SQLITE3 es una BBDD que viene ya embebida en python muy ligera que guarda la persistencia en el sistema
# Es decir crea un fichero binario en el directorio de la aplicacion donde almacena todo
import sqlite3

#Crear la bbdd y abir la conexion se hace en el mismo metodo
miConexion=sqlite3.connect("PrimeraBase")

#Para manejar estas BBDD hay que crear un cursor que es el que ejecuta querys
miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
miConexion.commit()

#Cerramos la conexion
miConexion.close()