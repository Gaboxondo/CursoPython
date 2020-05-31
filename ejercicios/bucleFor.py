for i in range(5):
    print("Bonjour")
    print(i)

for i in [1,2,3]:
    print("Hola")
    print(i)

for i in ["primavera", "verano", "otoño","invierno"]:
    print("Hello")
    print(i)

for i in ["pildoras","informaticas", 3]:
    print("Hola", end=" ")

print ("")

for i in "Hola":
    print(i)

#En un String va recorriendo cada caracter del string
contador = 0;
miEmail = input("Introduce tu direccion email: ")
for i in miEmail:
    if(i=="@" or i=="."):
        contador+=1
if contador >=2:
    print("Email correcto")
else:
    print("Email incorrecto")