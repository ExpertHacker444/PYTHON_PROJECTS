class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"mi habilidad es {self.habilida}")

class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, sueldo, empresa):
        Persona().__init__(self,nombre, edad, nacionalidad)
        Artista().__init__(self,habilidad)
        self.sueldo = sueldo
        self.empresa = empresa

    def presentarse(self):
        print(f"{super().mostrar_habilidad()}")


roberto = EmpleadoArtista("Roberto", 23, "Mexico", "Cantar", 1000000, "Cantica")

roberto.presentarse()


herencia = issubclass(EmpleadoArtista,Persona)
print(herencia)

instancia = isinstance(roberto, EmpleadoArtista)
print(instancia)
    

