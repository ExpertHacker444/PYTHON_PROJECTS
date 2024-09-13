class Clase:
    def __init__(self):
        self.__atributo_privados = "valores" #con el _ en self indicamos que esta variable sera privada si tiene _ se puede accede __mas seguro pero se puede 
        

objeto = Clase()
print(objeto.__atributo_privados)



