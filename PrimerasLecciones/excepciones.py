def suma(num1, num2):
    	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

#Aqui añadimos una captura de excepcion de dividido entre 0, es casi igualq ue ne java asi que no voy a poner mas detalle
def divide(num1,num2):
    try:
		return num1/num2
    except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operacion erronea"

#Aqui igual que ne java rodeamos un bloque no solo una operacion
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))
        break
    except ValueError:
        print("Los valoresintroducidos no son correctos")
	
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")