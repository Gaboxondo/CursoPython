print("Programa de becas año 2020")

distanciaEscuela=int(input("Introduce la distancia a la escuela en Km: "))
print(distanciaEscuela)

numeroHermanos=int(input("Introduce el nº de hermanos en el centro: "))
print(numeroHermanos)

salarioFamiliar=int(input("Introduce el salario familiar anual bruto: "))
print(salarioFamiliar)

if distanciaEscuela>40 and numeroHermanos>2 or salarioFamiliar<=20000:
    print("SI Tienes derecho a beca")
else:
    print("NO Tienes derecho a beca")
