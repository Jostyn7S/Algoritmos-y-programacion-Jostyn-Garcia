def calcular_pagos(monto_compra):
    if monto_compra > 5000000:
        inversion_empresa = 0.55 * monto_compra
        prestamo_banco = 0.30 * monto_compra
        credito_fabricante = 0.15 * monto_compra
    else:
        inversion_empresa = 0.70 * monto_compra
        prestamo_banco = 0
        credito_fabricante = 0.30 * monto_compra
    
    intereses = 0.20 * credito_fabricante
    
    return {
        "Inversión de la empresa": inversion_empresa,
        "Crédito con el fabricante": credito_fabricante,
        "Monto de intereses": intereses,
        "Préstamo del banco": prestamo_banco
    }

# Ejemplo de uso
monto_compra = float(input("Ingrese el monto total de la compra en COP: "))
resultado = calcular_pagos(monto_compra)

for clave, valor in resultado.items():
    print(f"{clave}: ${valor:,.2f} COP")