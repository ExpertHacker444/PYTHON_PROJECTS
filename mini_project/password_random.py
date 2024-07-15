import random
import tkinter as tk

def generar_contraseña(numero):
    digitos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%[&()]*+-?_"
    contraseñas = []

    for _ in range(numero):
        password = ''.join(random.choices(digitos, k=10))
        contraseñas.append(password)

    return contraseñas

def mostrar_contraseñas():
    numero_contraseñas = int(entry.get())
    contraseñas_generadas = generar_contraseña(numero_contraseñas)

    result_text.delete(1.0, tk.END)  # Limpiar el resultado anterior

    for password in contraseñas_generadas:
        result_text.insert(tk.END, f"{password}\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")

# Crear elementos de la interfaz
label = tk.Label(root, text="Número de Contraseñas a Generar:")
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generar Contraseñas", command=mostrar_contraseñas)
generate_button.pack()

result_text = tk.Text(root, height=10, width=30)
result_text.pack()

# Ejecutar la aplicación
root.mainloop()