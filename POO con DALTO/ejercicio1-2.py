from urllib.request import CacheFTPHandler


class Estudiante:
    def __init__(self, nombre, edad, ano):
        self.nombre = nombre
        self.edad = edad
        self.ano = ano

    def estudiar(self):
        print("Estudiante en curso...")

  
nombre = input("ingrese su nombre:")
edad = input("ingrese su edad: ")
ano = input("ingrese su año: ")

estudiantes = Estudiante(nombre, edad, ano)

print(f"""
      Datos del Estudiante: \n
      Nombre: {estudiantes.nombre}
      Edad: {estudiantes.edad}
      Año: {estudiantes.ano}
""")

while True:
    estudiar1 = input("esta estudiando? Ingrese la palabras estudiar: ")
    if estudiar1 == "estudiar":
        estudiantes.estudiar()
