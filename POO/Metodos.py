'''todas las funcion que creemos dentro de una clase son metodos
osea nos van a servir para crea las acciones que hagan nuestros objetos'''

class Celular:
    def __init__(self, nombre, marca): #metodo constructor
        self.nombre = nombre 
        self.marca = marca

    def llamar(self): #dentro de la clase Celular definimos el metodo llamar. Se agrega self para que reconozca el objeto
        print("Estas haciendo una llamada")

    def cortar(self): #lo mismo pero cortando la llamada
        print("finalizo la llamada")
    
    '''Los metodos que se crearon anteriormene de la clase Celular son las funcionalidades
     que podran realizar nuestros objetos '''

celular1 = Celular("Motorola", "m30")
celular2 = Celular("Samsung", "s20")

print(celular1.llamar())















