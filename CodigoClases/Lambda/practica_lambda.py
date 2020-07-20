'''
def area_triangulo(base,altura):
    return (base*altura)/2

#Imaginamos una aplicacion que hace calculos trigonometricos y vamos a usar el area de triangulo 1000 veces
# Con lambda funciones sencillos se pueden simplificar aun mas, si son complejas no se va a poder usar lambda
# para simplificar

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)
print(triangulo1)
print(triangulo2)
'''

#No pueden tener condicionales, bucles, etc. Solo un calculo
area_tringulo=lambda base,altura: (base*altura)/2

print(area_tringulo(5,7))
print(area_tringulo(9,6))