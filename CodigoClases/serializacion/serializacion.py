import pickle

lista_nombres = ["Pedro","Ana","Maria","Paco"]
fichero_binario = open("lista_nombres","wb")
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()
del fichero_binario

fichero_lectura = open("lista_nombres","rb")
lista = pickle.load(fichero_lectura)
print(lista)
fichero_lectura.close()
del fichero_lectura