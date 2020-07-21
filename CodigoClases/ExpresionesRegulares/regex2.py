import re

listaNombres=['Ana Gómez','María Martín','Sandra López','Santiago Martín','Sandra Fernández']
listaDominios=['http://pildorasinformaticas.es','ftp://pildorasinformaticas.es',
               'http://pildorasinformaticas.com','ftp://pildorasinformaticas.com',
               'http://infromaticaespaña.es','http://holaño.es']
listaRandom=['Hombres','Mujeres','niños','niñas','camion','camión']

print()
for elemento in listaNombres:
    if re.findall('^Sandra',elemento):
        print(elemento)

print()
for elemento in listaNombres:
    if re.findall('Martín$', elemento):
        print(elemento)

print()
for elemento in listaDominios:
    if re.findall('.es$', elemento):
        print(elemento)

print()
for elemento in listaDominios:
    if re.findall('^ftp', elemento):
        print(elemento)

print()
#Con corchetes busca si encuentra todos los caracteres que se les pongan dentro, ojo en cualquier sitio y orden
for elemento in listaDominios:
    if re.findall('[ñ]', elemento):
        print(elemento)

print()
for elemento in listaRandom:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)

print()
for elemento in listaRandom:
    if re.findall('cami[oó]n', elemento):
        print(elemento)