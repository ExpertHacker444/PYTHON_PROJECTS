def decorador (funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")

    return(funcion_modificada)

# def saludo():
#     print("hola man")

# saludito = decorador(saludo)
# saludito()

@decorador
def saludo():
    print("hola man") 

saludo()

#decordor de clase y multimples
    
