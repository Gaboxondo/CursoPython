import re

nombre1="Jara López"
nombre2="44324534252345345"
nombre3="a34234454"

if re.match(".ara",nombre3,re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

if re.match("\d",nombre2,re.IGNORECASE):
    print("Hemos encontrado una cadena que empieza por un numero")
else:
    print("No lo hemos encontrado")

if re.search("López",nombre1,re.IGNORECASE):
    print("Hemos encontrado cadena Lopez")
else:
    print("No lo hemos encontrado")