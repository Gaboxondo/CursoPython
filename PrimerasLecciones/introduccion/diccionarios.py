#Son HashMaps de java
miDiccionario={"Alemania":"Berlin","Francia":"Paris","Reino unido":"Londres","España":"Madrid"}
print(miDiccionario)

#Sacar el valor de la clave
print(miDiccionario["Francia"])
print(miDiccionario["España"])

#No asustarse por el error, es aposta
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
#Asi se sobreescribe de facil
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar elemento
miDiccionario={"Reino unido":"londres","España":"Madrid"}
print(miDiccionario)

#Diccionarios multiType
miDiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(miDiccionario2)

#Uso de tuplas con diccionarios
miTupla=("España","Francia","Reino unido","Alemania")
miDiccionario={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miTupla)
print(miDiccionario)
print(miDiccionario["Francia"])
print(miDiccionario[miTupla[1]])

#Diccionarios con listas
miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario)
print(miDiccionario["anillos"])

#Convertir diccionario dentro de otro, parece casi mas un Json
miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario)
print(miDiccionario["anillos"])

#Metodos utiles propios de los diccionarios
print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))