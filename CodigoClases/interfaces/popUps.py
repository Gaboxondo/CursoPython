from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Menu")

def infoAdicional():
    messagebox.showinfo("Procesador de Gabi","Procesador de textos version 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salirAplicacion():
    valor = messagebox.askokcancel("Salir","¿Estas seguro de que deseas cerrar la aplicacion?")
    if valor:
        root.destroy()

def cerrarDocuemnto():
    valor = messagebox.askretrycancel("Reintentar","No es posible cerrar, documento bloqueado")
    if not valor:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300,height=300)

#El tear off quita un separador feo que se ve por defecto
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocuemnto)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)

#Aqui le he dejado sin el tearoff para que se vea que es
archivoAyuda=Menu(barraMenu)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=lambda :infoAdicional())

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()