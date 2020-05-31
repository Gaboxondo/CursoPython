for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra " + letra)

print("")

nombre = "Pildoras informaticas"
print(nombre)
contador = 0
for i in nombre:
    if i==" ":
        continue
    contador +=1

print("Tamaño total de la cadena: " + str(len(nombre)))
print("Numero de letras: " + str(contador))

print("")

#Introduccion de un else dentro de un bucle en python no es un else de condicional OJO
#Este else de bucle se ejecuta cuando ya en el bucle no queda nada que recorres, aqui con el break no dejamos terminar
#por lo que no se ejecuta el else
email=input("Introduce tu email: ")
for i in email:
    if i == "@":
        arroba=True
        break
else:
    arroba=False

print(arroba)

#El pass deja el programa en espera hasta cancelar el programa
while True:
    pass