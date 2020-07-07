from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("File chooser")

def abreFichero():

    #Esto devuelve la ruta de fichero
    fichero = filedialog.askopenfilename(title="Abrir",initialdir="C:", filetypes=(("Ficheros excel","*.xlsx"),
                                                                                   ("Ficheros de texto","*.txt")))
    print(fichero)

Button(root, text="Abrir fichero",command=abreFichero).pack()

root.mainloop()