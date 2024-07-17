import random
import tkinter as tk

# Definir las opciones de la ruleta
opciones_ruleta = ["Descuento del 10%", "Descuento del 20%", "Corte de Pelo Gratis", "Corte de Pelo con 50% de descuento"]

def ruleta_aleatoria():
    # Seleccionar aleatoriamente una opción de la ruleta
    opcion_seleccionada = random.choice(opciones_ruleta)
    return opcion_seleccionada

def comenzar_ruleta():
    opcion_ganadora = ruleta_aleatoria()
    resultado_label.config(text=f"¡Felicidades! Has ganado: {opcion_ganadora}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Ruleta Aleatoria")

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.pack(pady=20)

# Botón para comenzar la ruleta
comenzar_button = tk.Button(root, text="Comenzar", command=comenzar_ruleta, font=("Arial", 12))
comenzar_button.pack(pady=10)

root.mainloop()