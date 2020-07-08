import sqlite3

bbdd=sqlite3.connect("GestionProductosConIdsNumeros")

miCursor=bbdd.cursor()

miCursor.execute('''
CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
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

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", variosProductos)

bbdd.commit()
bbdd.close()