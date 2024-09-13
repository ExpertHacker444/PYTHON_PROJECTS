import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('turnos.db')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Crear la tabla "turnos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS turnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT,
        medico TEXT,
        paciente TEXT,
        fecha DATE,
        hora TIME,
        consulta TEXT
    )
''')

# Crear la ventana
ventana = tk.Tk()
ventana.title('Tabla de Turnos')

# Crear la tabla
tabla = ttk.Treeview(ventana, columns=('id', 'dni', 'medico', 'paciente', 'fecha', 'hora', 'consulta'), show='headings')
tabla.heading('id', text='ID')
tabla.heading('dni', text='DNI')
tabla.heading('medico', text='Médico')
tabla.heading('paciente', text='Paciente')
tabla.heading('fecha', text='Fecha')
tabla.heading('hora', text='Hora')
tabla.heading('consulta', text='Consulta')
tabla.pack()

# Crear los campos de entrada
dni_label = tk.Label(ventana, text='DNI:')
dni_label.pack()
dni_entry = tk.Entry(ventana)
dni_entry.pack()

medico_label = tk.Label(ventana, text='Médico:')
medico_label.pack()
medico_entry = tk.Entry(ventana)
medico_entry.pack()

paciente_label = tk.Label(ventana, text='Paciente:')
paciente_label.pack()
paciente_entry = tk.Entry(ventana)
paciente_entry.pack()

fecha_label = tk.Label(ventana, text='Fecha:')
fecha_label.pack()
fecha_entry = tk.Entry(ventana)
fecha_entry.pack()

hora_label = tk.Label(ventana, text='Hora:')
hora_label.pack()
hora_entry = tk.Entry(ventana)
hora_entry.pack()

consulta_label = tk.Label(ventana, text='Consulta:')
consulta_label.pack()
consulta_entry = tk.Entry(ventana)
consulta_entry.pack()

# Crear el botón para insertar un nuevo turno
def insertar_turno():
    try:
        dni = dni_entry.get()
        medico = medico_entry.get()
        paciente = paciente_entry.get()
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        consulta = consulta_entry.get()

        # Insertar el nuevo turno en la base de datos
        cursor.execute('INSERT INTO turnos (dni, medico, paciente, fecha, hora, consulta) VALUES (?, ?, ?, ?, ?, ?)', 
                       (dni, medico, paciente, fecha, hora, consulta))
        conn.commit()

        # Limpiar los campos de entrada
        dni_entry.delete(0, tk.END)
        medico_entry.delete(0, tk.END)
        paciente_entry.delete(0, tk.END)
        fecha_entry.delete(0, tk.END)
        hora_entry.delete(0, tk.END)
        consulta_entry.delete(0, tk.END)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Turno agregado", "El turno ha sido agregado correctamente")

        # Actualizar la tabla
        tabla.delete(*tabla.get_children())
        cursor.execute('SELECT * FROM turnos')
        turnos = cursor.fetchall()
        for turno in turnos:
            tabla.insert('', 'end', values=(turno[0], turno[1], turno[2], turno[3], turno[4], turno[5], turno[6]))
    except Exception as e:
        messagebox.showerror("Error", str(e))

insertar_button = tk.Button(ventana, text='Insertar Turno', command=insertar_turno)
insertar_button.pack()

# Crear el botón para eliminar un turno
def eliminar_turno():
    try:
        # Obtener el ID del turno seleccionado
        seleccionado = tabla.selection()[0]
        id_turno = tabla.item(seleccionado, 'values')[0]

        # Eliminar el turno de la base de datos
        cursor.execute('DELETE FROM turnos WHERE id = ?', (id_turno,))
        conn.commit()

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Turno eliminado", "El turno ha sido eliminado correctamente")

        # Actualizar la tabla
        tabla.delete(*tabla.get_children())
        cursor.execute('SELECT * FROM turnos')
        turnos = cursor.fetchall()
        for turno in turnos:
            tabla.insert('', 'end', values=(turno[0], turno[1], turno[2], turno[3], turno[4], turno[5], turno[6]))
    except IndexError:
        messagebox.showerror("Error", "No se ha seleccionado un turno")

eliminar_button = tk.Button(ventana, text='Eliminar Turno', command=eliminar_turno)
eliminar_button.pack()

# Iniciar la aplicación
ventana.mainloop()

# Cerrar la conexión a la base de datos
conn.close()