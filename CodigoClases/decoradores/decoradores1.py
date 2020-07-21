# los decoradors son funciones que añaden funcionalidad a otras funciones
# Los decoradores estan formadas por 3 funciones A,B y C donde A recibe como parametro a B (otra funcion) para
# devolver otra funcion C (Un poco lio pero se vera bien en el ejemplo)
# En java son anotaciones

#Decorador super sencillo sin utilidad como ejemplo
# imaginemos un programa de 20 funciones en las que queremos agregar a TODAS o ALGUNAS una funcionalidad extra
# Aqui veremos tambine que *args significa que la funcion recibe un numero indeterminado de argumentos
# **kwards pasa claves valores
def funcionDecoradora(funcion_parametro):
    def funcionInterna(*args,**kwargs):
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo: ")
        funcion_parametro(*args,**kwargs)
        print("Se ha terminado el calculo")

    return funcionInterna

#Con esto se indica a python que decore la funcion
@funcionDecoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)

@funcionDecoradora
def resta(num1,num2):
    print(num1-num2)

@funcionDecoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(7,5,8)

resta(12,10)

#Por esto hay que añadir el **kwards por que viaja con clave valor
potencia(base=5,exponente=3)