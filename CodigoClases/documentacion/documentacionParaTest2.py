import doctest
import math

# Los ... en los test significan que puede venir lo que sea ahi, y se pueden hacer test con bucles
def raizCuadraraLista(listaNumeros):
    """
    La funcion devuelve una lista con las raices cuadradas de los elementos
    :param listaNumeros: Lista de numeros
    :return: Lista de las raices cuadradad

    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadraraLista(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4,-9,16]:
    ...     lista.append(i)
    >>> raizCuadraraLista(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """

    return [math.sqrt(n) for n in listaNumeros]

print(raizCuadraraLista([9,16,25,36]))
doctest.testmod()