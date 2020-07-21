import doctest
# aqui vamos a ver el uso de >>> para un text dentro de la documentacion
def areaTrangulo(base, altura):
    """
    Calcula el area de un triangulo segun su base y altura
    :param base: Longitud de la base del triangulo
    :param altura: Longitud del area del cuadrado
    :return: Cadena de texto con la informacion de area del triangulo
    >>> areaTrangulo(3,6)
    9.0
    """
    return (base * altura) / 2

def areaTranguloTestMal(base, altura):
    """
    Calcula el area de un triangulo segun su base y altura
    :param base: Longitud de la base del triangulo
    :param altura: Longitud del area del cuadrado
    :return: area del triangulo
    >>> areaTranguloTestMal(3,6)
    25.0
    """
    return (base * altura) / 2

def areaTranguloTestMalString(base, altura):
    """
    Calcula el area de un triangulo segun su base y altura
    :param base: Longitud de la base del triangulo
    :param altura: Longitud del area del cuadrado
    :return: Cadena de texto con la informacion de area del triangulo
    >>> areaTranguloTestMalString(3,6)
    'Es area del traingulo es: 9.0'

    >>> areaTranguloTestMalString(4,5)
    'Es area del traingulo es: 11.0'

    >>> areaTranguloTestMalString(9,3)
    'Es area del traingulo es: 13.5'
    """
    return "Es area del traingulo es: " + str((base * altura) / 2)

def comprobarMail(mail):
    """
    Busca la Arroba
    :param mail: email del usuario como string
    :return: true o false en funcioon de si solo hay una @ al final
    >>> comprobarMail('juanCursos@gmail.com')
    True

    >>> comprobarMail('juanCursos.com')
    False

    >>> comprobarMail('juanCursos.com@')
    False

    >>> comprobarMail('juanCursos@gmail@.com')
    False
    """
    arroba=mail.count('@')
    if arroba != 1 or mail.rfind('@')==len(mail)-1 or mail.find('@') == 0:
        return False
    else:
        return True

#Si estan todos los test bien no sale nada
doctest.testmod()