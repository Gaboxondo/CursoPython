from tkinter import *

root=Tk()
root.title("Labels")

miFrame = Frame(root,width=500,height=400)
miFrame.pack()

#miLabel = Label(miFrame,text="Hola alumnos de python")
# Al empaquetar el label adapta el tamaño
#miLabel.pack()
# Con place no empaqueta y redimensiona si no que lo pone en una posicion concreta
#miLabel.place(x=100,y=200)

# si con el label no vamos a hacer mucho mas se puede abreviar
Label(miFrame,text="hola alumnos de python",fg="red",font=("Comic Sanz MS",18)).place(x=100,y=300)

miImagen=PhotoImage(file="bob.gif")
Label(miFrame,image=miImagen).place(x=0,y=10)
#Tkinter solo trabaja con PNG y gif
root.mainloop()