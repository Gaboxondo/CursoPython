import re

listaNombres=['Ana','Pedro','María','Rosa','Sandra','Celia']
listaCiudades=['Ma1','Se1','Ma2','Ba1','Ma3','Va1','Va2','Ma4','MaA','Ma5','MaB']

print()
#Rangos desde la o a la t Distingue mayusculas y minusculas
for elemento in listaNombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)

print()
#Asi se ponen varios rangos
for elemento in listaCiudades:
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)

print()
#Rango negado es añadiendole delante ^ (seria no de 0 a 3)
for elemento in listaCiudades:
    if re.findall('Ma[^0-3]', elemento):
        print(elemento)