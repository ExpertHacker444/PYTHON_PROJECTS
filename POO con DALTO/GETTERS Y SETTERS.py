
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
   


personita = Persona("Lucas", 21)

nombre = personita.get_nombre()

print(nombre)

personita.set_nombre("MAESTRO")


