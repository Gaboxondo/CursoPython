class Coche:

    # Asi se crea el constructor, siempre con __init__
    # Para ponerlo solo accesoble desde la clase (COmo un privado en java es añadirle un __ (asi se encapsula)
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    # El self es lo mismo que en java el This pero hay que ponerlo en java esto es mas facil por uqe ya te viene el
    # this dado
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if self.__enmarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas. Un ancho de", self.__anchoChasis,"y un largo de",
              self.__largoChasis)


#   ---------------- CODIGO --------------

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("\n---------- A continucacion creamos el segundo objeto ----------\n")

miCoche2=Coche()
print(miCoche2.arrancar(False))
# Esta variable al estar encapsulada no tiene nada que ver, pero no falla, ya se vera por que
miCoche2.ruedas=2

#Se puede ver que las ruedas siguen siendo 4
miCoche2.estado()
