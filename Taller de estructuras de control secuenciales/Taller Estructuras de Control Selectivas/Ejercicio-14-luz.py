def calcular_pago_energia(lectura_anterior, lectura_actual):
    consumo = lectura_actual - lectura_anterior
    monto = 0
    
    if consumo <= 100:
        monto = consumo * 4600
    elif consumo <= 300:
        monto = (100 * 4600) + ((consumo - 100) * 80000)
    elif consumo <= 500:
        monto = (100 * 4600) + (200 * 80000) + ((consumo - 300) * 100000)
    else:
        monto = (100 * 4600) + (200 * 80000) + (200 * 100000) + ((consumo - 500) * 120000)
    
    return monto

# Solicitar datos al usuario
lectura_anterior = float(input("Ingrese la lectura anterior del medidor: "))
lectura_actual = float(input("Ingrese la lectura actual del medidor: "))

# Verificar que las lecturas sean válidas
if lectura_actual < lectura_anterior:
    print("Error: La lectura actual no puede ser menor que la anterior.")
else:
    monto_total = calcular_pago_energia(lectura_anterior, lectura_actual)
    print(f"El monto a pagar por el consumo de energía eléctrica es: {monto_total:,.2f} COP")

