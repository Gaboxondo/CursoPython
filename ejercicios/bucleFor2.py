for i in range(5):
    print(f"valor de la variable {i}")

print("")

for i in range(5,10):
    print(f"valor de la variable {i}")

print("")

for i in range(5,10,2):
    print(f"valor de la variable {i}")

#Devuelve la longitud de la cadena
len("Gabi")

#Otra manera mas rara y complicada de validar el mail
#Pero es por saber otra manera con len()
valido = False
email = input("Introduce el mail: ")
for i in range(len(email)):
    if email[i] == "@":
        valid = True
if valido:
    print("Email correcto")
else:
    print("Email Incorrecto")