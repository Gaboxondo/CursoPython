salarioPresidente=int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salarioPresidente))

salarioDirector=int(input("Introduce salario director: "))
print("Salario presidente: " + str(salarioDirector))

salarioJefeArea=int(input("Introduce salario jefe de area: "))
print("Salario presidente: " + str(salarioJefeArea))

salarioAdministrativo=int(input("Introduce salario administrativo: "))
print("Salario presidente: " + str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
    print("Todo funciona correctamente")
else:
    print("Algo huele mal")
