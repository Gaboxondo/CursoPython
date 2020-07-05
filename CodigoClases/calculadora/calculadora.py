from tkinter import *

raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("calculadora.ico")
raiz.resizable(0, 0)

miFrame = Frame(raiz)
miFrame.pack()

# --------------------------  VARIABLES GLOBALES --------------------------
operacion=""
resultado=0

# --------------------------  PANTALLA --------------------------
numeroPantalla = StringVar()

pantalla = Entry(miFrame, width=16, font=("Consolas", 18), textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

# --------------------------  PULSACIONES TECLAS NUMERICAS --------------------------
def numeroPulsado(num):

    global operacion

    print("Numero pulsado:",num)
    print("Operacion actual:", operacion)
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        if numeroPantalla.get() == "0" and num != ".":
            pass
        elif num == "." and numeroPantalla.get() == "":
            pass
        else:
            numeroPantalla.set(numeroPantalla.get() + num)

# --------------------------  FUNCION SUMA --------------------------
def suma(num):
    global operacion
    global resultado

    resultado+=float(num)
    operacion="suma"
    numeroPantalla.set(resultado)

# --------------------------  FUNCION RESTA --------------------------
#TODO: POR HACER, YA QUE NO FUNCIONA BIEN
def resta(num):
    global operacion
    global resultado

    resultado-=float(num)
    operacion="resta"
    numeroPantalla.set(resultado)

# --------------------------  FUNCION MULTIPLICACION --------------------------
#TODO: POR HACER, YA QUE NO FUNCIONA BIEN
def multiplicacion(num):
    global operacion
    global resultado

    resultado = resultado * float(num)
    operacion="multiplicacion"
    numeroPantalla.set(resultado)

# --------------------------  FUNCION IGUAL --------------------------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    resultado = 0

# --------------------------  BOTONES --------------------------
# --------------------------  fila1 --------------------------
boton7 = Button(miFrame, text="7", width=7, height=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=5, height=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=5, height=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=5, height=3)
botonDiv.grid(row=2, column=4)

# --------------------------  fila2 --------------------------
boton4 = Button(miFrame, text="4", width=7, height=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=5, height=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=5, height=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMul = Button(miFrame, text="*", width=5, height=3, command=lambda: multiplicacion(numeroPantalla.get()))
botonMul.grid(row=3, column=4)

# --------------------------  fila3 --------------------------
boton1 = Button(miFrame, text="1", width=7, height=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=5, height=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=5, height=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRes = Button(miFrame, text="-", width=5, height=3, command=lambda: resta(numeroPantalla.get()))
botonRes.grid(row=4, column=4)

# --------------------------  fila4 --------------------------
boton0 = Button(miFrame, text="0", width=7, height=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=".", width=5, height=3, command=lambda: numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=5, height=3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonSuma = Button(miFrame, text="+", width=5, height=3, command=lambda: suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

raiz.mainloop()
