miLista=["Maria","Pepe","Marta","Antonio"]

print("\nObtencion de objetos o trozos de lista")
print(miLista[2])
print(miLista[-2])
print(miLista[-3])

print(miLista[0:3])
print(miLista[1:3])
print(miLista[1:])
print(miLista[:])

print("\nAppend")
miLista.append("Manolo")
print(miLista)

print("\nInsert")
miLista.insert(2,"Paco")
print(miLista)

print("\nRemove")
miLista.remove("Antonio")
print(miLista)

print("\nExtend")
miLista.extend(["Juan","Sandra","Ana"])
print(miLista)

print("\nPop")
miLista.pop()
print(miLista)

print("\nIndex o Juan")
print(miLista.index("Juan"))

miLista=["Maria","Pepe","Marta","Maria"]
print("\nIndex o Maria con")
print(miLista.index("Maria"))

print("\nCheck Pepe y Manolo con IN")
print("Pepe" in miLista)
print("Manolo" in miLista)

print("\nListas multi tipo")
miLista=["Maria",5,True,6.8]
print(miLista)

miLista2=["Sandra","Lucia"]
print(miLista2)

print("\nConcatenacion de listas")
miLista3=miLista+miLista2
print(miLista3)

print("\nMultiplicacion de listas")
miLista = miLista*3
print(miLista)
