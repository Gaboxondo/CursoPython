print("Asignaturas optativas Año 2020")
print("Asignaturas optativas: Informatica grafica - Pruebas de sotware - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower();

if asignatura in ("informatica grafica".lower(),"pruebas de sotware".lower(),"usabilidad y accesibilidad".lower()):
    print("Asignatura elegida: " + asignatura)
else:
    print("Opcion no válida")
