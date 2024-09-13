class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) #llamamos al constructor de la clase padre
        self.trabajo = trabajo
        self.salario = salario

class Alumnos(Persona):
    def __init__(self, nombre, edad, nacionalidad, carrera, promedio):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.promedio = promedio

class Profesor(Persona):
    def __init__(self, nombre, edad, nacionalidad, cargo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.cargo = cargo
        self.sueldo = sueldo

#En este caso se puede ver como las demas clases dependen de la clase Padre (Persona)



roberto = Empleado("Roberto", 23, "Mexico", "programador", 100000)
print(roberto.nombre, roberto.edad, roberto.nacionalidad, roberto.trabajo, roberto.salario)