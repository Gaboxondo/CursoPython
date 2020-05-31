import math

i=1

while i<=10:
    print("Ejecuccion " + str(i))
    i+=1

print("Termino la ejecucion")
#-----------------------------------------------------

edad=int(input("Introduce tu edad por favor: "))
while edad<0 or edad>100:
    print("Has introducido una edad negativa.")
    edad=int(input("Introduce tu edad por favor: "))
print("Gracias")
print("Edad del aspirante: " + str(edad))
#-----------------------------------------------------

print("Calculo de la raiz cuadrara")
numero = int(input("Introduce un numero por favor: "))
intentos = 0
while numero <0:
    print("No se puede hallar la raiz de un numero negatico")
    if(intentos == 2):
        print("Ya has hecho muchos intentos de coña, se acabó")
        break
    numero = int(input("Introduce un numero por favor: "))
    if numero < 0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))