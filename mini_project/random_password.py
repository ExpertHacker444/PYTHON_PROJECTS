import random

def crear_contraseña(numero):
    digitos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%[&()]*+-?_"
    contraseñas = []

    for _ in range(numero):
        password = ''.join(random.choices(digitos, k=10))
        contraseñas.append(password)

    return contraseñas

contraseñas_generadas = crear_contraseña(2)

html_output = "<!DOCTYPE html>\n<html>\n<head>\n<style>\n.password-list {\nlist-style-type: none;\nmargin: 0;\npadding: 0;\n}\n.password-item {\nbackground-color: #f4f4f4;\nmargin: 5px;\npadding: 10px;\nborder-radius: 5px;\n}\n</style>\n</head>\n<body>\n<h1>Contraseñas Generadas</h1>\n<ul class='password-list'>"

for password in contraseñas_generadas:
    html_output += f"<li class='password-item'>{password}</li>"

html_output += "</ul>\n</body>\n</html>"

print(html_output)