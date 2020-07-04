from tkinter import *

root=Tk()
root.title("Entry")

miFrame = Frame(root,width=1200,height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre = Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red", justify="center")

#Texto con un scroll
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
#Asi se posiciona a la derecha del texto
scrollVert.grid(row=4, column=2, sticky="nse")
#Asi se setea que el posicionador nos indique en que punto estamos para que no se mueva solo
textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e",padx=10,pady=10)

comentariosLabel = Label(miFrame,text="Comentarios")
comentariosLabel.grid(row=4,column=0, sticky="e",padx=10,pady=10)

def codigoBoton():
    miNombre.set("Gabi")

# Lo hemos puesto en la raiz por cambiar un poco y ver el posicionamiento
botonEnvio = Button(root,text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()