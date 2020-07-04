from tkinter import *

root=Tk()
root.title("Entry")

miFrame = Frame(root,width=1200,height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
#Esta comentado por que se va a usar el grid
# cuadroTexto.place(x=100,y=100)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

nombreLabel = Label(miFrame,text="Nombre:")
#Esto no vale y es super complejo hacerlo asi, hay que usar el grid
#Vemos el nuevo paramtro de configuracion sticky que es la alineacion del texto
nombreLabel.grid(row=0,column=0, sticky="e",padx=10,pady=10)

passLabel = Label(miFrame,text="Contraseña:")
passLabel.grid(row=1,column=0, sticky="e",padx=10,pady=10)

apellidoLabel = Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=2,column=0, sticky="e",padx=10,pady=10)

direccionLabel = Label(miFrame,text="Direccion de casa:")
direccionLabel.grid(row=3,column=0, sticky="e",padx=10,pady=10)

root.mainloop()