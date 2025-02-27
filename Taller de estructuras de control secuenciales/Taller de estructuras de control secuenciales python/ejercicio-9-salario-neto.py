#Entradas
HorasTrabajadas = float(input("Ingrese el número de horas trabajadas: "))
PrecioHora = float(input("Ingrese el precio por hora trabajada: "))

#Caja negra
SalarioBruto = HorasTrabajadas * PrecioHora
Descuento = SalarioBruto * 0.20
SalarioNeto = SalarioBruto - Descuento

#Salidas
print("El salario bruto es: " , SalarioBruto)
print("El descuento por impuestos es: ", Descuento)
print("El salario neto a recibir es: " , SalarioNeto)