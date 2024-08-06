import json
import time
import os

with open("DatosPrecios.json", encoding="utf-8") as openfile:
    PrecioPan=json.load(openfile)

Bol=True
while Bol==True:
    print("==========================\n1).Vender\n2).Comprar\n3).Salir\n==========================")

    Opcion1=input(str("Ingrese un numero para ir a la opcion deseada: "))
    if Opcion1=="1":
        print("==========================\n1).Panaderia\n2).Pasteleria\n3).Bebidas\n4)Promociones\n5)Salir\n==========================")
        Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))
        if Opcion2=="1":
            print("========Panaderia========")
            for i in PrecioPan["Panaderia"]:
                print(i, "          Precio:",PrecioPan["Panaderia"][i])
                

    elif Opcion1=="2":
        print("==========================\n1).Vender\n2).Comprar\n3).Salir\n==========================")
        Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))
        if Opcion2=="1":
            print("")

print("jaja")
