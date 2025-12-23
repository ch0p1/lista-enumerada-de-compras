from datetime import date
fecha = date.today()

lista_c = []
print (f"Hoy es {fecha}  asi que compra la cena navideña 🎅")
print ("Cuando acabes escribe:  listo ")

while True:
   print ("1 Crear lista de compras")
   print ("2 añadir productos a tu lista")
   print ("3 crear nueva lista")
   print ("4 salir")
   opc= input(":")
   
   if opc == 1:
       print ("Escribe listo cuando termines")
       while True:
           comp= input()
           lista_c.append(comp)
           if comp == "listo":
               break
       break
    elif opc == 2:
        if not lista_c:
            print("No hay lista creada aún.")
            continue
   elif opc == 3:
       lista_c = []
   elif opc == 4:
       break

print ("\n Lista de compras cena navideña") 
for i, comp in enumerate (lista_c, start=1):
    print (i, comp)
        

