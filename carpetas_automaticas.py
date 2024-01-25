import os
import tkinter as tk
from tkinter import filedialog, messagebox

historial_carpetas = []  # Lista para almacenar el historial de carpetas abiertas

def crear_carpeta(event=None):
    nombre_carpeta = entrada_carpeta.get()
    ruta_principal = entrada_ruta.get()

    if nombre_carpeta and ruta_principal:
        ruta_carpeta = os.path.join(ruta_principal, nombre_carpeta)
        try:
            os.makedirs(ruta_carpeta)
            messagebox.showinfo("Éxito", f"La carpeta '{nombre_carpeta}' ha sido creada correctamente.")
        except FileExistsError:
            messagebox.showerror("Error", f"La carpeta '{nombre_carpeta}' ya existe.")
    else:
        messagebox.showerror("Error", "Por favor ingresa tanto el nombre de la carpeta como la ruta principal.")

def seleccionar_carpeta():
    ruta_seleccionada = filedialog.askdirectory()
    if ruta_seleccionada:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta_seleccionada)
        if ruta_seleccionada not in historial_carpetas:
            historial_carpetas.append(ruta_seleccionada)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Crear Carpeta")

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Establecer el ancho y alto de la ventana
ancho_ventana = 380
alto_ventana = 200

# Calcular la posición para centrar la ventana
posicion_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
posicion_y = (alto_pantalla // 2) - (alto_ventana // 2)

# Establecer la geometría de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

# Etiqueta y entrada para la ruta de la carpeta principal
etiqueta_ruta = tk.Label(ventana, text="Ruta de la carpeta principal:")
etiqueta_ruta.pack()
entrada_ruta = tk.Entry(ventana, width=50)
entrada_ruta.pack()

# Botón para seleccionar la carpeta principal
boton_seleccionar = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta)
boton_seleccionar.pack()

# Etiqueta y entrada para el nombre de la carpeta
etiqueta_carpeta = tk.Label(ventana, text="Nombre de la nueva carpeta (Ejm: 2024-01-25):")
etiqueta_carpeta.pack()
entrada_carpeta = tk.Entry(ventana)
entrada_carpeta.pack()

# Vincular la función crear_carpeta al evento <Return> para la entrada de nombre de carpeta
entrada_carpeta.bind("<Return>", crear_carpeta)

# Botón para crear la carpeta
boton_crear = tk.Button(ventana, text="Crear Carpeta", command=crear_carpeta)
boton_crear.pack()

# Ejecutar la ventana
ventana.mainloop()
