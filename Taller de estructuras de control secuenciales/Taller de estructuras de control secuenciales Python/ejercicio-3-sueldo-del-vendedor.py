#Entradas
SueldoBase=int(input("Ingrese el sueldo base del vendedor: "))
Venta1=int(input("Ingrese el monto de la primer venta: "))
Venta2=int(input("Ingrese el monto de la segunda venta: "))
Venta3=int(input("Ingrese el monto de la tercer venta: "))

#Caja negra
Comisiones = (Venta1+Venta2+Venta3)*0.10
SueldoTotal = (SueldoBase+Comisiones)

#Salidas
print("El total de comisiones es: ", Comisiones)
print("El sueldo total del vendedor es: ", SueldoTotal)