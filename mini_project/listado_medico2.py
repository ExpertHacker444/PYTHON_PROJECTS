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
        medico TEXT,
        paciente TEXT,
        fecha DATE,
        hora TIME,
        consulta TEXT
    )
''')

# Confirmar las modificaciones
conn.commit()

# Crear la ventana
ventana = tk.Tk()
ventana.title('Turnos del Médico')

# Función para cargar los turnos en la tabla
def cargar_turnos(medico):
    tabla_turnos.delete(*tabla_turnos.get_children())
    cursor.execute('SELECT * FROM turnos WHERE medico = ?', (medico,))
    turnos = cursor.fetchall()
    for turno in turnos:
        tabla_turnos.insert('', 'end', values=(turno[0], turno[2], turno[3], turno[4], turno[5]))

# Función para agregar un turno
def agregar_turno():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title('Agregar Turno')

    tk.Label(ventana_agregar, text='Fecha:').grid(row=0, column=0)
    fecha_entry = tk.Entry(ventana_agregar)
    fecha_entry.grid(row=0, column=1)

    tk.Label(ventana_agregar, text='Hora:').grid(row=1, column=0)
    hora_entry = tk.Entry(ventana_agregar)
    hora_entry.grid(row=1, column=1)

    tk.Label(ventana_agregar, text='Consulta:').grid(row=2, column=0)
    consulta_entry = tk.Entry(ventana_agregar)
    consulta_entry.grid(row=2, column=1)

    def guardar_turno():
        fecha = fecha_entry.get()
        hora = hora_entry.get()
        consulta = consulta_entry.get()

        cursor.execute('INSERT INTO turnos (medico, fecha, hora, consulta) VALUES (?, ?, ?, ?)', (medico, fecha, hora, consulta))
        conn.commit()
        cargar_turnos(medico)
        ventana_agregar.destroy()

    tk.Button(ventana_agregar, text='Guardar', command=guardar_turno).grid(row=3, column=0, columnspan=2)

# Función para eliminar un turno
def eliminar_turno():
    try:
        seleccionado = tabla_turnos.selection()[0]
        id_turno = tabla_turnos.item(seleccionado, 'values')[0]
        cursor.execute('DELETE FROM turnos WHERE id = ?', (id_turno,))
        conn.commit()
        cargar_turnos(medico)
        messagebox.showinfo("Turno eliminado", "El turno ha sido eliminado correctamente")
    except IndexError:
        messagebox.showerror("Error", "No se ha seleccionado un turno")

# Crear la tabla de turnos
tabla_turnos = ttk.Treeview(ventana, columns=('id', 'paciente', 'fecha', 'hora', 'consulta'), show='headings')
tabla_turnos.heading('id', text='ID')
tabla_turnos.heading('paciente', text='Paciente')
tabla_turnos.heading('fecha', text='Fecha')
tabla_turnos.heading('hora', text='Hora')
tabla_turnos.heading('consulta', text='Consulta')
tabla_turnos.pack()

# Función para inicializar la aplicación
def inicializar_aplicacion(medico):
    medico_label = tk.Label(ventana, text=f'Turnos del Médico: {medico}')
    medico_label.pack()

    cargar_turnos(medico)
    eliminar_button = tk.Button(ventana, text='Eliminar Turno', command=eliminar_turno)
    eliminar_button.pack()

# Obtener el nombre del médico
medico = 'Médico'

# Iniciar la aplicación
inicializar_aplicacion(medico)

# Iniciar la aplicación
ventana.mainloop()

# Cerrar la conexión a la base de datos
conn.close()