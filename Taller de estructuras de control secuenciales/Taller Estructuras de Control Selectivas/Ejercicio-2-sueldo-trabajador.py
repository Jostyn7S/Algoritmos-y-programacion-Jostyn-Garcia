def calcular_nuevo_sueldo(sueldo_bruto):
    # Definir el porcentaje de aumento
    if sueldo_bruto < 900000:
        aumento = 0.15
    else:
        aumento = 0.12
    
    # Calcular el nuevo sueldo
    nuevo_sueldo = sueldo_bruto * (1 + aumento)
    
    return nuevo_sueldo

# Solicitar al usuario el sueldo bruto
sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador en COP: "))

# Calcular el nuevo sueldo
nuevo_sueldo = calcular_nuevo_sueldo(sueldo_bruto)

# Imprimir el nuevo sueldo
print(f"El nuevo sueldo del trabajador es: ${nuevo_sueldo:,.2f} COP")

