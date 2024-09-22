import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Función para validar el formato de la hora
def validar_hora(hora):
    try:
        datetime.strptime(hora, '%H:%M')
        return True
    except ValueError:
        return False

# Función para agregar un evento
def agregar_evento():
    dia = dia_var.get()
    mes = mes_var.get()
    anio = anio_var.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if dia and mes and anio and hora and descripcion:
        if validar_hora(hora):
            fecha = f"{dia.zfill(2)} {mes} {anio}"
            tree.insert('', 'end', values=(fecha, hora, descripcion))
            limpiar_campos()
        else:
            messagebox.showwarning("Formato de Hora Inválido", "La hora debe tener el formato HH:MM.")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

# Función para eliminar un evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar el evento seleccionado?")
        if confirm:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("No seleccionado", "Por favor, seleccione un evento para eliminar.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    dia_var.set('')
    mes_var.set('')
    anio_var.set('')
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

# Función para limpiar toda la lista de eventos
def limpiar_lista():
    for item in tree.get_children():
        tree.delete(item)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("650x520")
root.configure(bg="#e1e2e1")

# Estilos personalizados
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=('Arial', 12, 'bold'), foreground="white", background="#4CAF50")
style.configure("Treeview", font=('Arial', 10), rowheight=25, background="#f9f9f9", foreground="#000000", fieldbackground="#f9f9f9")
style.configure("TButton", font=('Arial', 10, 'bold'), padding=6, background="#4CAF50", foreground="white")
style.map("TButton", background=[('active', '#45a049')])

# Frame principal para organizar los widgets
frame_principal = tk.Frame(root, bg="#e1e2e1")
frame_principal.pack(pady=20)

# Treeview para mostrar los eventos
tree = ttk.Treeview(frame_principal, columns=('Fecha', 'Hora', 'Descripción'), show='headings', height=10)
tree.heading('Fecha', text='Fecha')
tree.heading('Hora', text='Hora')
tree.heading('Descripción', text='Descripción')
tree.column('Fecha', width=150, anchor='center')
tree.column('Hora', width=100, anchor='center')
tree.column('Descripción', width=350)
tree.pack(side='left')

# Scrollbar para el Treeview
scrollbar = ttk.Scrollbar(frame_principal, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Frame para los campos de entrada
frame_entrada = tk.Frame(root, bg="#e1e2e1")
frame_entrada.pack(pady=10)

# Etiquetas y entradas para fecha, hora y descripción
tk.Label(frame_entrada, text="Día:", bg="#e1e2e1", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=10, pady=5)
dia_var = tk.StringVar()
dia_entry = ttk.Combobox(frame_entrada, textvariable=dia_var, values=[str(i) for i in range(1, 32)], state='readonly', width=5)
dia_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_entrada, text="Mes:", bg="#e1e2e1", font=('Arial', 10, 'bold')).grid(row=0, column=2, padx=10, pady=5)
mes_var = tk.StringVar()
meses_nombres = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes_entry = ttk.Combobox(frame_entrada, textvariable=mes_var, values=meses_nombres, state='readonly', width=12)
mes_entry.grid(row=0, column=3, padx=10, pady=5)

tk.Label(frame_entrada, text="Año:", bg="#e1e2e1", font=('Arial', 10, 'bold')).grid(row=0, column=4, padx=10, pady=5)
anio_var = tk.StringVar()
anio_entry = ttk.Combobox(frame_entrada, textvariable=anio_var, values=[str(i) for i in range(2024, 2031)], state='readonly', width=7)
anio_entry.grid(row=0, column=5, padx=10, pady=5)

tk.Label(frame_entrada, text="Hora (HH:MM):", bg="#e1e2e1", font=('Arial', 10, 'bold')).grid(row=1, column=0, padx=10, pady=5)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_entrada, text="Descripción:", bg="#e1e2e1", font=('Arial', 10, 'bold')).grid(row=2, column=0, padx=10, pady=5)
descripcion_entry = tk.Entry(frame_entrada, width=50)
descripcion_entry.grid(row=2, column=1, columnspan=5, padx=10, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root, bg="#e1e2e1")
frame_botones.pack(pady=20)

# Botón para agregar evento
btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

# Botón para eliminar evento seleccionado
btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

# Botón para limpiar toda la lista
btn_limpiar_lista = ttk.Button(frame_botones, text="Limpiar Lista", command=limpiar_lista)
btn_limpiar_lista.grid(row=0, column=2, padx=10)

# Botón para salir de la aplicación
btn_salir = ttk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=3, padx=10)

# Iniciar la aplicación
root.mainloop()
