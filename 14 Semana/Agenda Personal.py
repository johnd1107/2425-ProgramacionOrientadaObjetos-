import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def agregar_evento():
    """Agrega un nuevo evento a la lista."""
    fecha = entrada_fecha.get().strip()
    hora = entrada_hora.get().strip()
    descripcion = entrada_descripcion.get().strip()

    if fecha and hora and descripcion:
        evento = (fecha, hora, descripcion)
        lista_eventos.insert("", "end", values=evento)
        entrada_fecha.delete(0, tk.END)
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

def eliminar_evento():
    """Elimina el evento seleccionado de la lista."""
    seleccion = lista_eventos.selection()
    if seleccion:
        if messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?"):
            for item in seleccion:
                lista_eventos.delete(item)
    else:
        messagebox.showerror("Error", "Por favor, seleccione un evento.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Eventos")
root.geometry("600x400")  # Tamaño inicial de la ventana

# Frame para organizar los widgets
frame_principal = tk.Frame(root)
frame_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Etiquetas y campos de entrada para la fecha, hora y descripción
tk.Label(frame_principal, text="Fecha (Año-Mes-Día):").grid(row=0, column=0, sticky=tk.W, pady=5)
entrada_fecha = tk.Entry(frame_principal, width=20)
entrada_fecha.grid(row=0, column=1, pady=5)

tk.Label(frame_principal, text="Hora (Horas:Minutos):").grid(row=1, column=0, sticky=tk.W, pady=5)
entrada_hora = tk.Entry(frame_principal, width=20)
entrada_hora.grid(row=1, column=1, pady=5)

tk.Label(frame_principal, text="Descripción del Evento:").grid(row=2, column=0, sticky=tk.W, pady=5)
entrada_descripcion = tk.Entry(frame_principal, width=50)
entrada_descripcion.grid(row=2, column=1, pady=5)

# Treeview para mostrar los eventos
lista_eventos = ttk.Treeview(frame_principal, columns=("Fecha", "Hora", "Descripción"), show="headings", height=10)
lista_eventos.heading("Fecha", text="Fecha")
lista_eventos.heading("Hora", text="Hora")
lista_eventos.heading("Descripción", text="Descripción")
lista_eventos.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

# Frame para los botones
frame_botones = tk.Frame(frame_principal)
frame_botones.grid(row=4, column=0, columnspan=2, pady=10)

# Botones
tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).pack(side=tk.LEFT, padx=5)

root.mainloop()