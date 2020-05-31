print("Analizador de notas")

notaAlumno=int(input("Introduce tu nota: "))

if notaAlumno<5:
    print("Insuficiente, eres subnormal")
elif notaAlumno<6:
    print("Justito")
elif notaAlumno<7:
    print("Bien")
elif notaAlumno<9:
    print("Notable")
else:
    print("Sobresaliente")