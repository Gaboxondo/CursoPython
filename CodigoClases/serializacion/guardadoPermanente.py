import pickle


class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    listaPersonas = []

    def __init__(self):
        listaPersonasFile = open("ficheroExterno","ab+")
        listaPersonasFile.seek(0)

        try:
            self.listaPersonas=pickle.load(listaPersonasFile)
            print("Se cargaron {} personas del fichero externo".format(len(self.listaPersonas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaPersonasFile.close()
            del listaPersonasFile

    def agregarPersonas(self,p):
        self.listaPersonas.append(p)

    def mostrarPersonas(self):
        for p in self.listaPersonas:
            print(p)

    def save(self):
        listaPersonasFile = open("ficheroExterno","wb")
        pickle.dump(self.listaPersonas,listaPersonasFile)
        listaPersonasFile.close()
        del listaPersonasFile

miLista = ListaPersonas()
p=Persona("Manolo","Femenino",30)
miLista.agregarPersonas(p)
p=Persona("Gabi","Masculino",29)
miLista.agregarPersonas(p)
p=Persona("Paco","Masculino",56)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()
miLista.save()