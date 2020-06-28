
archivo_texto=open("archivo.txt","r")
print(archivo_texto.read())
# vemos que si volvemos a imprimir no sale nada, por que lee por puntero, una vez leido el puntero
# estara al final y ya no lee nada, habria que mandarlo al principio
print(archivo_texto.read())

#Asi se mueve el puntero de lectura a mno
archivo_texto.seek(0)
print(archivo_texto.read())

#Asi si lo movemos a lo loco
archivo_texto.seek(8)
print(archivo_texto.read())

#Se puede leer tmbn sllo hasta un caracter determinado
archivo_texto.seek(0)
print(archivo_texto.read(11))
#Si ahora volvemos a leer el puntero lee del 11 en adelante
print(archivo_texto.read())

#Esto no se que cojones le pasa que da 0
print("IMPRESION DE LA MITAD")
archivo_texto.seek(0)
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())

#Asi leemos quitando la primera linea
archivo_texto.seek(0)
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())

archivo_texto.close()

#Asi abre el archivo desde la primera linea, asi que si escribimos
# subsstituyendo los caracteres de la piemra linea
archivo_texto_dos=open("archivo.txt","r+")
archivo_texto_dos.write("Comienzo de texto")
print(archivo_texto_dos.read())

archivo_texto_dos.seek(0)
lista_text=archivo_texto_dos.readlines()
lista_text[2]="Esta linea ha sido incluido por la cara\n"
archivo_texto_dos.writelines(lista_text)
archivo_texto_dos.close()