import re

cadena="Vamos a aprender expresiones regulares"
textoBuscar="aprender"

if re.search(textoBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

textoEncontrado = re.search(textoBuscar,cadena)

#Numero del primer caracter donde encuentra el texto
print(textoEncontrado.start())
#Numero del ultimo caracter donde encuentra el texto
print(textoEncontrado.end())
#lo mismo de antes pero me da las dos en un arreglo
print(textoEncontrado.span())

cadena="Vamos a aprender expresiones regulares en python. Python es un lenguaje de programacion"
textoBuscar="python"
print(len(re.findall(textoBuscar.upper(),cadena.upper())))