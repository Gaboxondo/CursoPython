#Construyen a diferencia de una funcion, que contruye toda la lista por ejemplo de numeros pares
# Contruye un Iterable con el primer numero (2) y entra en un estado de standBy volviendo el flujo de ejecucion
# Si se vuelve a llamar, construiria el segundo numero (4) y vuelve al standby devolviendo el flujo de ejecucion.
# y asi sucesivamente , ¿Por que?, por que es mas eficiente, a lo mejor no necesitamos los 40 primeros numeros pares

def generaPares(limite):
    num=1
    miLista=[]
    while num<limite+1:
        miLista.append(num*2)
        num+=1
    return miLista

def generaParesGen(limite):
    num=1
    while num<limite+1:
        yield num*2
        num+=1

#Con funcion
print(generaPares(10))
print("")

#Con generador
devuelvePares=generaParesGen(10)
print(next(devuelvePares))
print("Codigo de por medio")
print(next(devuelvePares))
print("Codigo de por medio")
print(next(devuelvePares))
print("")

#Tambien se puede recorrer devuelvePares en un bucle
devuelvePares=generaParesGen(10)
for i in devuelvePares:
    print(i)

#Al generador se le puede quitar el limite ya que no es una funcion y no generaria infinitos numeros