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

miCursor.execute("SELECT * FROM PRODUCTOS")
productos=miCursor.fetchall()
print(productos)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Jugueteria'")
productos=miCursor.fetchall()
print(productos)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'Camiseta'")
bbdd.commit()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_ARTICULO = 'Camiseta'")
productos=miCursor.fetchall()
print(productos)

miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO = 'Camiseta'")
bbdd.commit()

miCursor.execute("SELECT * FROM PRODUCTOS")
productos=miCursor.fetchall()
print(productos)

bbdd.close()