saldo = 1000

while True:
    print("Cajero Automático")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        deposito = float(input("Ingrese la cantidad a depositar: "))
        if deposito > 0:
            saldo += deposito
            print("Depósito exitoso. Saldo actual:", saldo)
        else:
            print("Cantidad no válida.")

    elif opcion == "2":
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if 0 < retiro <= saldo:
            saldo -= retiro
            print("Retiro exitoso. Saldo actual:", saldo)
        else:
            print("Fondos insuficientes o cantidad no válida.")

    elif opcion == "3":
        print("Saldo actual:", saldo)

    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intente de nuevo.")