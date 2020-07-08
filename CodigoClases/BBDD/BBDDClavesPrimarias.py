import sqlite3

bbdd=sqlite3.connect("GestionProductos")

miCursor=bbdd.cursor()

miCursor.execute('''
CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20)
)
''')

variosProductos=[
    ("AR01","Camiseta",10,"Deportes"),
    ("AR02","Jarron",90,"Ceramica"),
    ("AR03","Destornillador",5,"Ferreteria"),
    ("AR04","Camióm",20,"Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",variosProductos)

bbdd.commit()
bbdd.close()


bbdd2=sqlite3.connect("GestionProductosConIdsNumeros")

miCursor2=bbdd2.cursor()

miCursor2.execute('''
CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20)
)
''')

variosProductos=[
    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Ceramica"),
    ("Destornillador",5,"Ferreteria"),
    ("Camióm",20,"Jugueteria")
]

miCursor2.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",variosProductos)

bbdd2.commit()
bbdd2.close()