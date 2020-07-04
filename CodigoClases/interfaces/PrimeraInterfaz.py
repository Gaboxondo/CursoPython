from tkinter import Tk

# Crea la ventana
raiz = Tk()
# Le da titulo
raiz.title("Ventana de prueba")
# Permite o no el redimensionamiento en un eje y otro
raiz.resizable(1,True)
# Le añade el iconito
raiz.iconbitmap("bob.ico")
# Le setea el tamaño
raiz.geometry("650x360")
# Le da un fondo azul
raiz.config(bg="blue")
# Esto hay que ponerlo siempre para que no se cierre el programa
raiz.mainloop()