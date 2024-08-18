class Celular:
    def __init__(self, marca, modelo, color): #funcion contructora (init metodo constructor)
        self.marca = marca                    #objeto(celular1).marca sera = a lo que agreguemos en marca
        self.modelo = modelo
        self.color = color

celular1 = Celular("Motorola", "m22", "Rojo") #se crea la instancia de celular osea el objeto
celular2 = Celular("Samsung", "s22", "Negro")

print(celular1.color) #imprime el atributo color de la instacia (celular1) se lo llama con .color
print(celular2.modelo)
