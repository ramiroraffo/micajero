def cajero():
    print("Hola Bienvenido al cajero de codo a codo")
    idioma = int(input("ingresa \n 1 para elegir el idioma en español \n 2 para ingles \n 3 para portugues\n"))
    if idioma == 1:
        print("has seleccionado el idioma español")
        print("Ingresa tu clave para acceder a tu cuenta \nla clave es 1234 ")
        clave = int(input("ingresa tu clave: "))
        nombre = str(input("ingresa tu nombre: "))
        if clave == 1234:
            saldo = float(85200)
            saldoDolar = float(0)
            movimientos= []
            print("#########################################################")
            print(f"Hola {nombre} seleciona una opcion y presiona lo siguiente: ")
            print("#########################################################")
            print("     #1  consultar saldo en pesos")
            print("     #2  consultar saldo en dolares")
            print("     #3  depositar pesos")
            print("     #4  extraer pesos")
            print("     #5  transferir pesos")
            print("     #6  comprar dolares")
            print("     #7  extraer dolares")
            print("     #8  transferir dolares")
            print("     #9  vender dolares")
            print("     #10 crear plazo fijo")
            print("     #11 ver ultimos movimientos")
            print("     #12 salir de la cuenta")
            print("#########################################################")
            opcion=0
            while (opcion:=str(input("introduce una opción: "))) != "12":
                #opciones
                def opciones():
                    input("Enter para continuar ")
                    print("#########################################################")
                    print(f"{nombre}, Desea realizar otra operacion? ")
                    print("#########################################################")
                    print("     #1  consultar saldo en pesos")
                    print("     #2  consultar saldo en dolares")
                    print("     #3  depositar pesos")
                    print("     #4  extraer pesos")
                    print("     #5  transferir pesos")
                    print("     #6  comprar dolares")
                    print("     #7  extraer dolares")
                    print("     #8  transferir dolares")
                    print("     #9  vender dolares")
                    print("     #10 crear plazo fijo")
                    print("     #11 ver ultimos movimientos")
                    print("     #12 salir de la cuenta")
                    print("#########################################################")

                #1consultar saldo en pesos
                if opcion == "1":
                    print(f"#########################################################\nSu saldo actual en pesos es de: AR${saldo}")
                    opciones()
                
                #2Consultar saldo en dolares
                elif opcion == "2":
                    print(f"#########################################################\nSu saldo actual en dolares es de: US${saldoDolar}")
                    opciones()
                
                #3depositar pesos
                elif opcion == "3":
                    print("#########################################################")
                    ingreso = int(input("Digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: AR$ "))
                    if ingreso > 0:
                        saldo+= ingreso
                        print(f"#########################################################\nGracias por ingresar su dinero, su saldo actual es de: ${saldo}")
                        movimientos.append(f"Deposito en pesos de AR${ingreso}")
                        opciones()
                    else:
                        print("#########################################################\nMonto incorrecto")
                        opciones()
                
                #4extraer pesos
                elif opcion == "4":
                    print("#########################################################")
                    extraccion = int(input("Ingrese el monto a extraer: AR$"))
                    if extraccion > saldo:
                        print("#########################################################\nSaldo Insuficiente")
                        opciones()
                    elif extraccion > 0:
                        saldo-= extraccion
                        print(f"#########################################################\nDinero extraido, tu saldo restante es: AR${saldo}")
                        movimientos.append(f"Extraccion en pesos de AR${extraccion}")
                        opciones()
                    else:
                        print("#########################################################\nMonto Incorrecto")
                        opciones()
                
                #5trasferir pesos
                elif opcion == "5":
                    print("#########################################################")
                    transferir = int(input("Ingrese el cbu de la cuenta a la cual deseas transferir: "))
                    monto = int(input("Ingresa el monto a tranferir: "))
                    if monto > saldo:
                        print("#########################################################\nSaldo insuficiente")
                        opciones()
                    elif monto > 0:
                        print("#########################################################")
                        print(f"Estas por realizar una transferencia al numero de cuenta {transferir} con el siguiente monto: AR${monto}, estas seguro que deseas realizar esta accion?")
                        confirmar = str(input("ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n"))
                        if confirmar == "si":
                            saldo-= monto
                            print(f"#########################################################\nSu transferencia ha sido realizada, su saldo actual es de: AR${saldo}")
                            movimientos.append(f"Transaccion en pesos a CBU:{transferir} de AR${monto}")
                            opciones()
                        elif confirmar == "no":
                            print("#########################################################\nHa cancelado Su transferencia")
                            opciones()
                        else:
                            print("#########################################################\nHa ingresado un valor invalido")
                            opciones()
                    else:
                        print("#########################################################\nMonto Incorrecto")
                        opciones()
                
                #6comprar dolares
                elif opcion == "6":
                    print("#########################################################")
                    print("        El precio del dolar es de $160")
                    print(f"        Su saldo es el siguiente: ${saldo}")
                    print("#########################################################")
                    compraDolar = float(input("Ingrese el monto de dolares a comprar: $"))
                    conversion = compraDolar * 160
                    if conversion > saldo:
                        print("#########################################################\nSaldo insuficiente")
                        opciones()
                    elif compraDolar > 0:
                        print("#########################################################")
                        print(f"Esta seguro de comprar : US${compraDolar}? AR${conversion} seran debitados de su cuenta")
                        confirma  = str(input("Ingrese \n     #si para confirmar. \n     #no para cancelar\n"))
                        if confirma == "si":
                            saldo-= conversion
                            saldoDolar+= compraDolar
                            print(f"#########################################################\nSu saldo en su cuenta pesos es de: AR${saldo}\nSu saldo en su cuenta dolares es de: US${saldoDolar}")
                            movimientos.append(f"Compra de dolares de US${compraDolar}")
                            opciones()
                        elif confirma == "no":
                            print("#########################################################\nHa cancelado su compra")
                            opciones()
                        else:
                            print("#########################################################\nOpcion Incorrecta")
                            opciones()
                    else:
                        print("#########################################################\nMonto Incorrecto")
                        opciones()

                #7extraer dolares
                elif opcion == "7":
                    extraccion = int(input("Ingrese el monto a extraer: US$"))
                    if extraccion > saldoDolar:
                        print("#########################################################\nSaldo Insuficiente")
                        opciones()
                    elif extraccion > 0:
                        saldoDolar-= extraccion
                        print(f"#########################################################\nDinero extraido, su saldo restante es: US${saldoDolar}")
                        movimientos.append(f"Extraccion en dolares de US${extraccion}")
                        opciones()
                    else:
                        print("#########################################################\nMonto Incorrecto")
                        opciones()

                #8transferir dolares
                elif opcion == "8":
                    transferir = int(input("Ingrese el cbu de la cuenta a la cual deseas transferir: "))
                    monto = int(input("Ingrese el monto a tranferir: "))
                    if monto > saldoDolar:
                        print("#########################################################\nSaldo insuficiente")
                        opciones()
                    elif monto > 0:
                        print(f"#########################################################\nEsta por realizar una transferencia al numero de cuenta {transferir} con el siguiente monto: US${monto}, esta seguro que desea realizar esta accion?")
                        confirmar = str(input("Ingrese: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n"))
                        if confirmar == "si":
                            saldoDolar-= monto
                            print(f"#########################################################\nSu transferencia ha sido realizada, su saldo actual es de: US${saldoDolar}")
                            movimientos.append(f"Transaccion en dolares a CBU:{transferir} de US${monto}")
                            opciones()
                        elif confirmar == "no":
                            print("#########################################################\nHa cancelado tu transferencia")
                            opciones()
                        else:
                            print("#########################################################\nHa ingresado un valor invalido")
                            opciones()
                    else:
                        print("#########################################################\nMonto Incorrecto")
                        opciones()

                #9vender dolares
                elif opcion == "9":
                    print(f"#########################################################\nSu saldo actual en dolares es de US${saldoDolar}\nEl precio de venta del dolar es de AR$155\n#########################################################")
                    ventaDolar= int(input("Ingrese cuantos dolares desea vender: "))
                    conversion= ventaDolar*155
                    if ventaDolar > saldoDolar:
                        print("#########################################################\nSaldo insuficiente")
                        opciones()
                    elif ventaDolar > 0:
                        print(f"Esta por vender {ventaDolar} dolares, AR${conversion} van a ser depositados en su cuenta")
                        confirmar = str(input("Ingrese: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
                        if confirmar == "si":
                            saldoDolar-= ventaDolar
                            saldo+= conversion
                            print(f"#########################################################\nSu transferencia ha sido realizada\nsu saldo actual en dolares es de: US${saldoDolar}\nsu saldo actual en pesos es de AR${saldo}")
                            movimientos.append(f"Venta de dolares de US${ventaDolar}")
                            opciones()
                        elif confirmar == "no":
                            print("#########################################################\nHa cancelado tu transferencia")
                            opciones()
                        else:
                            print("#########################################################\nHa ingresado un valor invalido")
                            opciones()
                    else:
                        print("#########################################################\nMonto Incorrecto")
                        opciones()
                        
                #10crear plazo fijo
                elif opcion == "10":
                    print(f"\n")
                    opciones()

                #11ultimos movimientos
                elif opcion == "11":
                    if len(movimientos) > 0:
                        print("Tus ultimos movimientos son:")
                        print(movimientos[:])
                        opciones()
                    else:
                        print("#########################################################\nNo hay movimientos")
                        opciones()
                else:
                    print("#########################################################\nOpcion Incorrecta")
                    opciones()
        else:
            print("clave incorrecta\n#########################################################")
    elif idioma == 2:
        print("has seleccionado ingles")
    elif idioma == 3:
        print("has seleccionado portugues")
    else:
        print("opcion incorrecta")
cajero()