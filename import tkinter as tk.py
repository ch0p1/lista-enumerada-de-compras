import tkinter as tk
from datetime import date
from tkinter import messagebox

# ---------------- DATOS ----------------
fecha = date.today()
lista_c = []

# ---------------- FUNCIONES ----------------
def crear_lista():
    lista_c.clear()
    lista_box.delete(0, tk.END)
    messagebox.showinfo("Lista", "Nueva lista creada")

def agregar_producto():
    producto = entrada.get()
    if producto == "":
        return
    lista_c.append(producto)
    lista_box.insert(tk.END, producto)
    entrada.delete(0, tk.END)

def mostrar_lista():
    if not lista_c:
        messagebox.showwarning("Lista vacía", "No hay productos en la lista")
        return

    texto = "Lista de compras:\n\n"
    for i, prod in enumerate(lista_c, start=1):
        texto += f"{i}. {prod}\n"

    messagebox.showinfo("Lista de Compras", texto)

def salir():
    ventana.destroy()

# ---------------- VENTANA ----------------
ventana = tk.Tk()
ventana.title("Lista de compras - Cena navideña 🎅")
ventana.geometry("400x400")

# ---------------- ELEMENTOS ----------------
titulo = tk.Label(
    ventana,
    text=f"Hoy es {fecha}\nCompra la cena navideña 🎄",
    font=("Arial", 12, "bold")
)
titulo.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

btn_agregar = tk.Button(ventana, text="Añadir producto", command=agregar_producto)
btn_agregar.pack(pady=5)

lista_box = tk.Listbox(ventana, width=40, height=10)
lista_box.pack(pady=10)

btn_crear = tk.Button(ventana, text="Crear nueva lista", command=crear_lista)
btn_crear.pack(pady=3)

btn_mostrar = tk.Button(ventana, text="Mostrar lista", command=mostrar_lista)
btn_mostrar.pack(pady=3)

btn_salir = tk.Button(ventana, text="Salir", command=salir)
btn_salir.pack(pady=10)

# ---------------- EJECUCIÓN ----------------
ventana.mainloop()
