import json
import datetimeE
import os

Bol=True
while Bol==True:

    with open("Info.json", encoding="utf-8") as openfile: 
        PrecioPan=json.load(openfile)

    with open("DatosVentas.json", encoding="utf-8") as openVenta:
        Ventas=json.load(openVenta)

    with open("DatosCompra.json", encoding="utf-8") as openCompra:
        Compras=json.load(openCompra)

    os.system("clear")
    print("==========================\n1).Vender\n2).Comprar\n3).Ver registros\n4).Salir\n==========================")
    Opcion1=input(str("Ingrese un numero para ir a la opcion deseada: "))
    if Opcion1=="1":
        NombreEmpleado=str(input("Ingrese su nombre de empleado: "))
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

                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrecioPan["Panaderia"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cantidad=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cantidad*PrecioPan["Panaderia"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NombreEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cantidad,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)
                        
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif Contador < 11:
                        os.system("clear")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")

            elif Opcion2=="2":
                os.system("clear")
                print("========Pasteleria========")
                for i in PrecioPan["Pasteleria"]:
                    print(i, "Precio:",PrecioPan["Pasteleria"][i])

                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrecioPan["Pasteleria"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cantidad=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cantidad*PrecioPan["Pasteleria"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NombreEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cantidad,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)
                        
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif Contador < 11:
                        os.system("clear")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            
            elif Opcion2=="3":
                os.system("clear")
                print("========Bebidas========")
                for i in PrecioPan["Bebidas"]:
                    print(i, "Precio:",PrecioPan["Bebidas"][i])

                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrecioPan["Bebidas"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cantidad=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cantidad*PrecioPan["Bebidas"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NombreEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cantidad,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)
                        
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif Contador < 10:
                        os.system("clear")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            
            elif Opcion2=="4":
                os.system("clear")
                print("========Apartado de promociones========")
                for i in PrecioPan["Apartado de promociones"]:
                    print(i, "Precio:",PrecioPan["Apartado de promociones"][i])

                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrecioPan["Apartado de promociones"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cantidad=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cantidad*PrecioPan["Apartado de promociones"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NombreEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cantidad,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)
                        
                        input("Producto añadido al carrito, presione Enter para continuar")
                    
                    elif Contador < 10:
                        os.system("clear")

                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            
            elif Opcion2=="5":
                os.system("clear")
                print("======Saliendo======")
                input("Presione Enter para continuar")
                bol1=False

    elif Opcion1=="2":
        bol1=True
        while bol1==True:
            os.system("clear")
            print("==========================\n1).Comprar\n2).Salir\n==========================")
            Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))
            if Opcion2=="1":
                NombreProovedor=str(input("Nombre del proovedor al que se le comprara: "))
                NumeroProovedor=int(input("Numero del proovedor al que desea comprar: "))
                NombreProducto=str(input("Que producto desea comprar: "))
                CantidadProducto=int(input("Cantidad del producto que desea comprar: "))
                PrecioProducto=int(input("Precio del producto que desea comprar: "))
                PrecioTotal=PrecioProducto*CantidadProducto
                Fecha=str(datetime.datetime.now())

                Compras[0]["Personas"].append(
                    {
                        "Fecha": Fecha,
                        "Nombre":NombreProovedor,
                        "Numero":NumeroProovedor,
                        "Producto":NombreProducto,
                        "Cantidad":CantidadProducto,
                        "Precio Unitario":PrecioProducto,
                        "Precio Total":PrecioTotal
                    }
                )
                with open("DatosCompra.json", "w") as files:
                    json.dump(Compras,files)

            elif Opcion2=="2":
                os.system("clear")
                print("======Saliendo======")
                input("Presione Enter para continuar")
                bol1=False

    elif Opcion1=="3":
        bol2=True
        while bol2==True:
            os.system("clear")
            print("==========================\n1).Registros ventas\n2).Registros Compras\n3).Salir\n==========================")         
            Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))

            if Opcion2=="1":
                os.system("clear")
                for i in Ventas[0]["Personas"]:
                    print("================Ventas==========================")
                    print("Fecha de compra: ",i["Fecha"],"\nDireccion: ",i["Nombre"],"\nEmpleado: ",i["Empleado"],"\nProducto: ",i["Producto"][0]["NombreP"],"\nCantidad: ",i["Producto"][0]["Cantidad"],"\nPrecio Venta : ",i["Producto"][0]["PrecioP"])
                    print("================================================")

                input("Presione Enter para continuar")    

            elif Opcion2=="2":
                os.system("clear")
                for i in Compras[0]["Personas"]:
                    print("==================Compras========================")
                    print("Fecha de compra: ",i["Fecha"],"\nNombre del proovedor: ",i["Nombre"],"\nProducto: ",i["Producto"],"\nCantidad: ",i["Cantidad"],"\nPrecio Total: ",i["Precio Total"])
                    print("=================================================")

                input("Presione Enter para continuar")

            elif Opcion2=="3":
                os.system("clear")
                print("======Saliendo======")
                input("Presione Enter para continuar")
                bol2=False


    elif Opcion1=="4":
        Bol=False