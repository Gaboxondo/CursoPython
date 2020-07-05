from tkinter import *

root=Tk()
root.title("Chekc box")

playa=IntVar()
montana=IntVar()
desierto=IntVar()

def opcionesViaje():
    opcionesEscogidas=""

    if playa.get()==1:
        opcionesEscogidas+=" playa"
    if montana.get()==1:
        opcionesEscogidas += " montaña"
    if desierto.get() == 1:
        opcionesEscogidas += " desierto"
    textoFinal.config(text=opcionesEscogidas)

foto=PhotoImage(file="plane.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elige Destinos",width=50).pack()

Checkbutton(frame,text="playa",variable=playa,onvalue=1,offvalue=0, command=lambda:opcionesViaje()).pack()
Checkbutton(frame,text="montaña",variable=montana,onvalue=1,offvalue=0, command=lambda:opcionesViaje()).pack()
Checkbutton(frame,text="desierto",variable=desierto,onvalue=1,offvalue=0, command=lambda:opcionesViaje()).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()