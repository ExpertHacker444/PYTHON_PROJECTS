#polimorfismo = muchasformas

class Gato():
    def sonido(self):
        return "Miauu"
    
class Perro():
    def sonido(self):
        return "Guauu"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

hacer_sonido(gato)




def recorrer (elemento):
    for item in elemento:
        print(f"el elemento es: {item}")

lista1 = [1,2,3,4]
lista2 = ["hola", "como", "estas"]

print(lista2)


def volar(plumas):
    for pluma in plumas:
        print(f"La {pluma} esta volando")

volar(["paloma", "gaviota"])





    
