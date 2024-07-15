import random

def crear_contraseña(numero):
    digitos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%[&()]*+-?_"

    for _ in range(numero):
        password = ''.join(random.choices(digitos, k=10))
        print(password)

crear_contraseña(2)


