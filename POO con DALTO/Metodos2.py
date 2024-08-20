


class Camara:
    def __init__(self, nombre, marca): #metodo constructor
        self.nombre = nombre 
        self.marca = marca

    def sacar(self): 
        print(f"Estas sacando una foto de : {self.marca}") #se agrega self para reconocer objeto y se llama la marca

    def borrar(self):
        print(f"Estas borrando una foto de : {self.nombre}")

camara1 = Camara("Motorola Pro", "m30")
camara2 = Camara("Samsung", "s20")

camara1.sacar()
camara1.borrar()

#__init__ este metodo constructor de caracter especial nos permite iniciar las propiedades/atributos de una clase. 
