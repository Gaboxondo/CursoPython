def devuelveMax(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1=input("Introduce el primer numero: ")
num2=input("Introduce el segundo numero: ")

print(devuelveMax(num1,num2))