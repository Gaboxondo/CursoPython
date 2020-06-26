# el raise lanza una excepcion propia, aqui como supuestamente no se han visto POO se lanza un 
# Typeerror que es un tipo de excepcion que se le puede pasar string de mierda
# Vamos que el raise es igual que el throw

# Ojo que aqui lanzamos la excepcion pero no la capturamos ni controlamos en la llamada al metodo,
# Ver excepciones4

def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        "Cuidate..."

edad = (int(input("Introduce tu edad: ")))
print(evaluaEdad(edad))
