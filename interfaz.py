import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

datos_guardados = []

def mensaje_bienvenida():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Mostrar mensaje.", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje", command=lambda: messagebox.showinfo("Bienvenida", "Hola Bienvenid@ al programa")).pack()

def ingreso_datos():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Identifique al alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Ingresa el nombre del alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Seleccione la opcion necesaria:").pack()
    opcion_elegida = tk.StringVar(value="Opción 1")
    tk.Radiobutton(area_dinamica, text="Femenino", variable=opcion_elegida, value="Femenino").pack()
    tk.Radiobutton(area_dinamica, text="Masculino", variable=opcion_elegida, value="Masculino").pack()

    tk.Label(area_dinamica, text="Materias:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Español", "Ingles", "Matetmáticas"])
    combo.pack()
    combo.current(0)


    etiqueta_datos = tk.Label(area_dinamica, text="", font=("Arial", 12), fg="black")
    etiqueta_datos.pack(pady=10)

    def accion_guardar():
        valor = campo_texto_uno.get()
        seleccion = opcion_elegida.get()
        lista = combo.get()

        datos_guardados.append(f"Nombre: {valor}, Selección: {seleccion}, Lista: {lista}")

        etiqueta_datos.config(text="\n".join(datos_guardados))

    tk.Button(area_dinamica, text="Guardar Datos", command=accion_guardar).pack(pady=5)


def color_ventana():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configura el color: ", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def interfaz_preguntas():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Preguntas del programa", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus propias palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("600x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=mensaje_bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ingreso de datos", command=ingreso_datos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ajustes de color", command=color_ventana, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Preguntas", command=interfaz_preguntas, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

mensaje_bienvenida()
ventana_principal.mainloop()
