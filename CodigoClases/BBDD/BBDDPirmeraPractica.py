#SQLITE3 es una BBDD que viene ya embebida en python muy ligera que guarda la persistencia en el sistema
# Es decir crea un fichero binario en el directorio de la aplicacion donde almacena todo
import sqlite3

#Crear la bbdd y abir la conexion se hace en el mismo metodo
miConexion=sqlite3.connect("PrimeraBase")

#Para manejar estas BBDD hay que crear un cursor que es el que ejecuta querys
miCursor=miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon',15,'Deportes')")

variosProductos=[
    ("Camiseta",10,"deportes"),
    ("Jarron",90,"Ceramica"),
    ("Camióm",20,"Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print("Nombre articulo: ",producto[0],"Precio:",producto[1],"Departamento:",producto[2])

#Cerramos la conexion
miConexion.close()