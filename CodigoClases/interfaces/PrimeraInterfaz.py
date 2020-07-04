from tkinter import *

# Crea la ventana
raiz = Tk()
# Le da titulo
raiz.title("Ventana de prueba")
# Permite o no el redimensionamiento en un eje y otro, lo comentamos para poder redimensaionar
#raiz.resizable(1,True)
# Le añade el iconito
raiz.iconbitmap("bob.ico")
# Le setea el tamaño, lo comentamos por que luego con el frame, la raiz se adapata al mismo
#raiz.geometry("650x360")
# Le da un fondo azul
raiz.config(bg="blue")
raiz.config(bd=45)
raiz.config(relief="groove")
raiz.config(cursor="hand2")

# Asi se crea el frame dentro de la ventana
miFrame=Frame()
# El frame hay que empaquetarlo, el side lo ancal a un lugar de la raiz.
# Anchor tambien es para posicionar, va con cardinales norte, sur este y oeste en ingles
# El fill hace que se autoadapte a un eje, si probamos con X hay que añadir el expand. Tambiens e puede usar fill both
miFrame.pack(side="left", anchor="s", fill="x", expand=True)
#Para verlo le damos un color de fondo pero hay que darle tamaño
miFrame.config(bg="red")
miFrame.config(width="650",height="350")
#Despues de esto redimensaionar para ver como se ve la raiz abajo, el fram tiene un tamaño fijo pero la raiz no

#Para cambiar el borde
miFrame.config(bd=15)
miFrame.config(relief="sunken")

#Para cambiar el cursor cuando se pasa por encima
miFrame.config(cursor="pirate")

# TODO LO QUE SE APLICA AL FRAME SE LE PUEDE APLICAR A LA RAIZ
# Esto hay que ponerlo siempre para que no se cierre el programa
raiz.mainloop()