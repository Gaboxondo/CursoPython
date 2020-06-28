print("Programa de evaluacion de notas de alumno")

nota_alumno=input("Introduce la nota del alumno: ")
print(nota_alumno)

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))