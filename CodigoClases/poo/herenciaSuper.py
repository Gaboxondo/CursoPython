class Persona:

    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print("Nombre:",self.nombre,"edad",self.edad,"Lugar de residencia",self.lugarResidencia)

class Empleado(Persona):

    def __init__(self,salario,antiguedad,nombre,edad,residencia):
        super().__init__(nombre,edad,residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:",self.salario,"Antiguedad:",self.antiguedad)

paco = Persona("Paco",34,"Colobia")
paco.descripcion()

antonio=Empleado(1500,15,"Antonio",55,"España")
antonio.descripcion()

#La funcion instance of de java pero en python, vemos que anto
print("¿Es antonio persona?",isinstance(antonio,Persona))
print("¿Es antonio empleado?",isinstance(antonio,Empleado))
print("¿Es antonio persona?",isinstance(paco,Persona))
print("¿Es antonio empleado?",isinstance(paco,Empleado))