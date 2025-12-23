from datetime import date
fecha = date.today()

lista_c = []
print (f"Hoy es {fecha}  asi que compra la cena navideña 🎅")
print ("Cuando acabes escribe:  listo ")

while True:
   comp= input("comprar: ")

   if comp.lower() == "listo":
      break
   
   lista_c.append(comp)

print ("\n Lista de compras cena navideña") 
for i, comp in enumerate (comp, start=1):
    
    print (i, comp)
