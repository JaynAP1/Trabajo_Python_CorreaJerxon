import json
import time
import os

with open("DatosPrecios.json", encoding="utf-8") as openfile:
    PrecioPan=json.load(openfile)

Bol=True
while Bol==True:
    os.system("clear")
    print("==========================\n1).Vender\n2).Comprar\n3).Salir\n==========================")

    Opcion1=input(str("Ingrese un numero para ir a la opcion deseada: "))
    if Opcion1=="1":
        bol1=True
        while bol1==True:
            os.system("clear")
            print("==========================\n1).Panaderia\n2).Pasteleria\n3).Bebidas\n4).Promociones\n5).Salir\n==========================")
            Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))

            if Opcion2=="1":
                os.system("clear")
                print("========Panaderia========")
                for i in PrecioPan["Panaderia"]:
                    print(i, "Precio:",PrecioPan["Panaderia"][i])

                input("Presiona Enter para continuar")

            elif Opcion2=="2":
                os.system("clear")
                print("========Pasteleria========")
                for i in PrecioPan["Pasteleria"]:
                    print(i, "Precio:",PrecioPan["Pasteleria"][i])

                input("Presiona Enter para continuar")
            
            elif Opcion2=="3":
                os.system("clear")
                print("========Bebidas========")
                for i in PrecioPan["Bebidas"]:
                    print(i, "Precio:",PrecioPan["Bebidas"][i])

                input("Presiona Enter para continuar")
            
            elif Opcion2=="4":
                os.system("clear")
                print("========Apartado de promociones========")
                for i in PrecioPan["Apartado de promociones"]:
                    print(i, "Precio:",PrecioPan["Apartado de promociones"][i])

                input("Presiona Enter para continuar")
            
            elif Opcion2=="5":
                os.system("clear")
                print("======Saliendo======")
                input("Presione Enter para continuar")
                bol1=False

    elif Opcion1=="2":
        os.system("clear")
        print("==========================\n1).Vender\n2).Comprar\n3).Salir\n==========================")
        Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))
        if Opcion2=="1":
            print("")

print("jaja")
