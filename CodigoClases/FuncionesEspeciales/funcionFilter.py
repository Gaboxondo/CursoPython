#La funcion filter verifica todos los elementos de una secuencia o lista que cumplen una condicion
# devolviendo un iterador de los que la cumplen

class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} y tiene un salario de {}".format(self.nombre,self.cargo,self.salario)

'''
def numeros_par(num):
    if(num % 2 == 0):
        return True
'''

numeros=[17,24,7,39,8,51,92]

# Lo hacemos con una lambda en lugar de la declaracion de la funcion
print(list(filter(lambda numero_par: numero_par%2 == 0,numeros)))

listaEmpleados=[
    Empleado("Juan","Director",75000),
    Empleado("Ana","Presidenta",85000),
    Empleado("Antonio","Administrativo",25000),
    Empleado("Sara","Secretaria",27000),
    Empleado("Mario","Botones",21000)
]

salarios_altos=filter(lambda empleado:empleado.salario > 50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)