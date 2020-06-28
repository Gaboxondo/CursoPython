class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando",
              self.acelera, "\nFrenando:", self.frena)

class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculo):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    #Sobreescritura de metodo
    def estado(self):
        #Mi duda, no hay un super para llamar al del padre y no escribir los veces lo mismo?
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando",
              self.acelera, "\nFrenando:", self.frena, "\nCaballito:",self.hcaballito)

class VElectricos(Vehiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Estamos heredadno tod incluido el instructor
miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

print("")

miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Cuando hay HERENCIA MULTIPLE, se da preferencia la clase que se coloca primero
#Esto realmente nunca lo hariamos asi, VElectricos deberia heredar de Vehiculos o algo asi
class BicicletaElectrica(VElectricos,Vehiculo):
    pass

print("")
miBici = BicicletaElectrica("Orbea","HC130")
miBici.estado()
