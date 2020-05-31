miTupla=("Juan",13,1,1995)

print(miTupla[2])
print(miTupla.index("Juan"))

miLista=list(miTupla)
print(miTupla)
print(miLista)

miLista2=["Manolo",18,3,1997]
miTupla2=tuple(miLista2);
print(miLista2)
print(miTupla2)

print("Juan" in miTupla)
print("Juan" in miTupla2)

print(miTupla.count(13))
miTupla=("Juan",13,13)
print(miTupla.count(13))

print(len(miTupla))
miTupla=(10,2,3,"manolo",5)
print(len(miTupla))

#Tupla unitaria (Hay que poner la cma, si no no es unitaria)
miTupla=("Juan",)

#Empaquetado de tupla (tupla sin parenteris)
miTupla="Juan",13,1,1995
print(miTupla)

#Desempaquetado de tupla
nombre, dia, mes, agno = miTupla
print(nombre)
print(mes)
print(dia)
print(agno)