class Celular(): #clase
    marca = "motorola" #atributos
    modelo = "m22"     
    color = "negro"

celular1 = Celular() #objeto celular1 
print(celular1.color)



class Celular:
    def __init__(self):
        self.marca = "motorola"
        self.modelo = "m22"
        self.color = "negro"

celular1 = Celular()
print(celular1.color)


