import tkinter as tk

# Crear la ventana principal
app = tk.Tk()
app.title("Aplicación GUI Básica")

# Agregar información a la lista
def add_info():
    info = entry.get()  # Obtiene el texto ingresado por el usuario
    if info:
        listbox.insert(tk.END, info)  # Agregar el texto a la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto

# Limpia la lista o la informacion seleccionada
def clear_info():
    listbox.delete(0, tk.END)  # Limpiar todos los elementos de la lista

# Componentes de la ventana principal
title_label = tk.Label(app, text="Ingresa la información porfavor:", font=("Arial", 14))
title_label.pack(pady=10)  # Muestra la etiqueta con un poco de espacio alrededor

entry = tk.Entry(app, font=("Arial", 12))
entry.pack(pady=5)  # Campo de texto donde el usuario puede ingresar datos

add_button = tk.Button(
    app,
    text="Agregar",
    font=("Arial", 12),
    bg="#00a8e8",
    fg="white",
    command=add_info,  # Llamar a la funcion 'add_info' al hacer clic
)
add_button.pack(pady=5)  # Boton para agregar la informacion

clear_button = tk.Button(
    app,
    text="Limpiar",
    font=("Arial", 12),
    bg="#e80000",
    fg="white",
    command=clear_info,  # Llamar a la funcion 'clear_info' al hacer clic
)
clear_button.pack(pady=5)  # Boton para limpiar la lista

listbox = tk.Listbox(app, font=("Arial", 12), height=10, width=50)
listbox.pack(pady=10)  # Lista para mostrar la informacion agregada

# Ejecutar la aplicacion
app.mainloop()
