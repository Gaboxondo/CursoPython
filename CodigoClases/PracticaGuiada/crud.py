from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
#------------------------- Funciones --------------------------#

def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE USUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(100),
                COMENTARIOS VARCHAR(200)
            )
        ''')
        messagebox.showinfo("BBDD","BBDD Creada con éxito")
    except:
        messagebox.showwarning("Error", "La BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("salir","¿Deseas salir de la aplicacion")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miId.set("")
    limpiarCamposMenosId()

def limpiarCamposMenosId():
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete(1.0,END)

def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
    #Aqui lo suyo es hacer la clase usuario y usar lo ?,?,? como en el ejemplo de BBDD BBDDCrud
    """
    miCursor.execute("INSERT INTO USUARIOS VALUES(NULL,'" + miNombre.get() + "','" + miPass.get() + "','" +
                     miApellido.get() + "','" + miDireccion.get() + "','" + textoComentario.get("1.0",END) + "')")
    """
    miCursor.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)",datos)

    miConexion.commit()
    messagebox.showinfo("BBDD","Regsitro insertado con exito")

def leer():
    limpiarCamposMenosId()
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM USUARIOS WHERE ID=" + miId.get())

    #Sabemos que como buscamos por Id solo hay uno pero devuelve siempre un array
    usuarios = miCursor.fetchall()
    for usuario in usuarios:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0,usuario[5])

    miConexion.commit()

def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)
    #Aqui lo suyo es hacer la clase usuario y usar lo ?,?,? como en el ejemplo de BBDD BBDDCrud
    """
    miCursor.execute("UPDATE USUARIOS SET " +
                     "NOMBRE_USUARIO='" + miNombre.get() +
                     "', PASSWORD='" + miPass.get() +
                     "', APELLIDO='" + miApellido.get() +
                     "', DIRECCION='" + miDireccion.get() +
                     "', COMENTARIOS='" + textoComentario.get("1.0",END) +
                     "' WHERE ID=" + miId.get())
    """
    miCursor.execute("UPDATE USUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=? WHERE ID =" + miId.get(), datos)
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con exito")

def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM USUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Regsitro Eliminado con exito")
    limpiarCampos()
#------------------------- Barra Menu --------------------------#

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Crud", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#------------------------- Campos --------------------------#

miFrame=Frame(root)
miFrame.pack()

# esto va a ser donde se almacena las variables de los entrys
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroId=Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nse")
textoComentario.config(yscrollcommand=scrollVert.set)

#------------------------- Labels --------------------------#

labelId=Label(miFrame,text="Id:")
labelId.grid(row=0,column=0,sticky="e",padx=10,pady=10)

labelNombre=Label(miFrame,text="Nombre:")
labelNombre.grid(row=1,column=0,sticky="e",padx=10,pady=10)

labelPassword=Label(miFrame,text="Password:")
labelPassword.grid(row=2,column=0,sticky="e",padx=10,pady=10)

labelApellido=Label(miFrame,text="Apellido:")
labelApellido.grid(row=3,column=0,sticky="e",padx=10,pady=10)

labelDireccion=Label(miFrame,text="Direccion:")
labelDireccion.grid(row=4,column=0,sticky="e",padx=10,pady=10)

labelComentaio=Label(miFrame,text="Comentario:")
labelComentaio.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#------------------------- Botones --------------------------#

frameBotones=Frame(root)
frameBotones.pack()

botonCrear=Button(frameBotones,text="Crear", command=crear)
botonCrear.grid(row=0,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(frameBotones,text="Leer", command=leer)
botonLeer.grid(row=0,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(frameBotones,text="Actualizar",command=actualizar)
botonActualizar.grid(row=0,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(frameBotones,text="Borrar",command=eliminar)
botonBorrar.grid(row=0,column=3,sticky="e",padx=10,pady=10)

root.mainloop()