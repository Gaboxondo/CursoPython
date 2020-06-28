class Coche:
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazaminetoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()
desplazaminetoVehiculo(miVehiculo)

miVehiculo2=Coche()
desplazaminetoVehiculo(miVehiculo2)

miVehiculo3=Moto()
desplazaminetoVehiculo(miVehiculo3)