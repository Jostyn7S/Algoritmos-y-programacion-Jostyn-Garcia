#Entrada
TotalCompra=int(input("Ingrese el total de la compra: "))

#Caja negra
Descuento=(TotalCompra*0.15)
TotalPago=(TotalCompra - Descuento)

#Salidas
print("El descuento es de: " , Descuento)
print("El total a pagar con el descuento es de: " , TotalPago)