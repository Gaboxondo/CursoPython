import modulodoc
#Poniendo triples comillas y con intro Pycharm ya te abre tado, se tiene que poner jutso dentro de la
# dfinicion de la funcion
# Para la documentacion de una clase se hace igual

class Areas:
    """
    Esta clase calcula las areas de cuadrado y triangulo con metodos
    """
    def areaCuadrado(lado):
        """
        Calcula el area de un cuadraro
        :param lado: longitud del area del cuadraro
        :return: Cadena de texto con la informacion de area del cuadrado
        """
        return "el area del cuadrado es: " + str(lado*lado)

    def areaTrangulo(base,altura):
        """
        Calcula el area de un triangulo segun su base y altura
        :param base: Longitud de la base del triangulo
        :param altura: Longitud del area del cuadrado
        :return: Cadena de texto con la informacion de area del triangulo
        """
        return "el area del triangulo es: " + str((base*altura)/2)


print(Areas.areaTrangulo(2,7))

#Asi imprime la documentacion
print(Areas.areaCuadrado.__doc__)
help(Areas.areaCuadrado)

print(Areas.__doc__)
help(Areas)

help(modulodoc)
