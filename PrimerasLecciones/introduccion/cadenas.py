nombreUsuario=input("Introduce tu nombre de usuario: ")
print("El nombre de usuario es:",nombreUsuario.upper())
print("El nombre de usuario es:",nombreUsuario.lower())
print("El nombre de usuario es:",nombreUsuario.capitalize())


edad=input("Introduce tu edad: ")
print(edad.isdigit())

while not edad.isdigit():
    print("Por favor introduce un valor numero")
    print(edad.isdigit())
    edad=input("Introduce tu edad: ")
if int(edad)<18:
    print("No se puede pasar")
else:
    print("Se puede pasar")