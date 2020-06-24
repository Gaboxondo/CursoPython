#excepts consecutivos igual que en java
#El finally igual que en java
# Tambiens e puede poner solo except: sin tipo de excepcion a modo de excepcion generico como en java el tipo Exception
def divide():

    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))

        print("La division es: " + str(op1/op2))
    except ValueError:
        print("El valor introducido es erroneo, introduce un numero")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        print("Calculo finalizado")

divide()