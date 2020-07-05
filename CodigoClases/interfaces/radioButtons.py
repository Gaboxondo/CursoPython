from tkinter import *

root=Tk()
root.title("Radio")

varOpcion=IntVar()

def imprimir():
    print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido Femenino")
    else:
        etiqueta.config(text="Has elegido Otros")

Label(root,text="Género:").pack()

Radiobutton(root,text="Masculino",variable=varOpcion,value=1, command=lambda:imprimir()).pack()
Radiobutton(root,text="Femenino",variable=varOpcion,value=2, command=lambda:imprimir()).pack()
Radiobutton(root,text="Otra opción",variable=varOpcion,value=3, command=lambda:imprimir()).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()