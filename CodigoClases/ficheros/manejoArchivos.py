from io import open

#Apertura tipo escritura para escribir
archivo_texto=open("archivo.txt","w")
frase="Estupendo dia para estudiar Python\nel domingo por la tarde\n"
archivo_texto.write(frase)
archivo_texto.close()

archivo_texto_lectura=open("archivo.txt","r")
#texto=archivo_texto_lectura.read()
#print(texto)
#archivo_texto_lectura.close()

#Asi se leen cada linea en un array lo que permite hacer muchas cosas
lineastexto=archivo_texto_lectura.readlines()
print(lineastexto)
print(lineastexto[0])
for linea in lineastexto:
    print(linea,end='')
    if "Python" in linea:
        print("contine python")
    else:
        print("no contiene python")

#Apertura en escritura, lectura (append)
archivo_texto_lectura_escritura=open("archivo.txt","a")
archivo_texto_lectura_escritura.write("Siempre es una buena ocasion para estudiar algo nuevo\n")
archivo_texto_lectura_escritura.close()