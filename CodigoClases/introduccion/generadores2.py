#Se explica el uso de yield from que simplifica el codigo cuando dentro de un generador hay que usar un bucle for
# por ejemplo si el generador devuelve objetos o arrays y queremos acceder a sus subelementos deberemos usar bucles dentro del generador anidados

#Un * indica que va a recibir un numero indeterminado de elementos y en forma de tupla

#Devolveremos solo ciudades que se le pasan
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudadesDevueltas = devuelveCiudades("Madrid","Barcelona","Malaga","Bilbao")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

#Se devuelve subelemento de las ciudades, en este caso las letras de cada ciudad
def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudadesDevueltas2 = devuelveCiudades2("Madrid","Barcelona","Malaga","Bilbao")

print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))


#Simplificacion del bucle for anidado dentro de un generador
def devuelveCiudades3(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudadesDevueltas3 = devuelveCiudades3("Madrid","Barcelona","Malaga","Bilbao")

print(next(ciudadesDevueltas3))
print(next(ciudadesDevueltas3))
print(next(ciudadesDevueltas3))
print(next(ciudadesDevueltas3))
print(next(ciudadesDevueltas3))
