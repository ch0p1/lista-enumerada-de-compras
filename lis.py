import tkinter as tk
from tkinter import messagebox
from datetime import date
fecha = date.today()

lista_c = []

print(f"Hoy es {fecha} así que compra la cena navideña 🎅")

while True:
    print("\n1 Crear lista de compras")
    print("2 Añadir productos a tu lista")
    print("3 Mostrar lista de compras")
    print("4 Salir")

    opc = input("Opción: ")

    if opc == "1":
        lista_c.clear()
        print("Escribe 'listo' cuando termines")
        while True:
            comp = input("Comprar: ")
            if comp.lower() == "listo":
                break
            lista_c.append(comp)

    elif opc == "2":
        if not lista_c:
            print("No hay lista creada aún.")
            continue
        while True:
            comp = input("Añade un producto (listo para terminar): ")
            if comp.lower() == "listo":
                break
            lista_c.append(comp)

    elif opc == "3":
        if lista_c:
            root = tk.Tk()
            root.withdraw()  # Oculta ventana principal
            mostrar_texto = ""
            for i, item in enumerate(lista_c, start=1):
                mostrar_texto += f"{i}. {item}\n"
            messagebox.showinfo("Lista de Compras", mostrar_texto)
            root.destroy()
        else:
            print("La lista está vacía.")
    elif opc == "4":
        break

    else:
        print("Opción no válida.")

print("\nLista de compras cena navideña:")
for i, comp in enumerate(lista_c, start=1):
    print(i, comp)


