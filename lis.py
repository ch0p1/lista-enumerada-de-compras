from datetime import date
fecha = date.today()

lista_c = []

print(f"Hoy es {fecha} así que compra la cena navideña 🎅")

while True:
    print("\n1 Crear lista de compras")
    print("2 Añadir productos a tu lista")
    print("3 Crear nueva lista")
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
        lista_c.clear()
        print("Lista reiniciada.")

    elif opc == "4":
        break

    else:
        print("Opción no válida.")

print("\nLista de compras cena navideña:")
for i, comp in enumerate(lista_c, start=1):
    print(i, comp)
