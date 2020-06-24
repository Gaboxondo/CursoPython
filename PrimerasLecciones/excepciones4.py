# Aqui vamos a ver como capturar la excepcion con un nombre e imprimir su mensaje

import math

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

numero=(float(input("Introduce un numero: ")))
try:
    print(calculaRaiz(numero))
except ValueError as error:
    print(error)

print("Programa finalizado")