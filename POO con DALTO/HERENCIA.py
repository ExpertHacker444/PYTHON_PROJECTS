class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print(f"hola me llamo {self.nombre} soy de {self.nacionalidad}")

      

roberto = Persona("Roberto", 23, "Mexico")

roberto.hablar() #llamamos al metodo hablar

print(roberto.edad) #imprimimos edad

'''la clase Empleado hereda de la clase Persona dentro del parametro y ya
se le puso pass para referir a que no se rompa el programa y se lo pone como
indefinido y esta hereda de la clase Persona'''
        
        