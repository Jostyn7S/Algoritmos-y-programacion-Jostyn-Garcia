def calcular_incentivos(ventas_deptos, salario_bruto):
    total_ventas = sum(ventas_deptos)
    umbral_incentivo = 0.33 * total_ventas
    incentivo = 0.20 * salario_bruto
    pagos = []
    
    for ventas in ventas_deptos:
        if ventas > umbral_incentivo:
            pagos.append(salario_bruto + incentivo)
        else:
            pagos.append(salario_bruto)
    
    return pagos

# Ejemplo de uso
ventas_deptos = [float(input(f"Ingrese las ventas del departamento {i+1}: ")) for i in range(3)]
salario_bruto = float(input("Ingrese el salario bruto mensual de los vendedores: "))

pagos_finales = calcular_incentivos(ventas_deptos, salario_bruto)

for i, pago in enumerate(pagos_finales, 1):
    print(f"Pago final para vendedores del departamento {i}: ${pago:,.2f} COP")