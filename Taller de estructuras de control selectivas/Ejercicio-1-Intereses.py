def calcular_interes(capital_inicial, tasa_interes_anual, umbral_reinversion):
    # Calcular los intereses generados
    intereses_generados = capital_inicial * (tasa_interes_anual / 100)

    # Verificar si los intereses generados exceden el umbral de reinversión
    if intereses_generados > umbral_reinversion:
        # Reinvertir los intereses
        capital_final = capital_inicial + intereses_generados
    else:
        # No reinvertir los intereses
        capital_final = capital_inicial

    return intereses_generados, capital_final

# Datos de entrada
capital_inicial = float(input("Introduzca el capital inicial (en COP): "))
tasa_interes_anual = float(input("Introduzca la tasa de interés anual (en %): "))
umbral_reinversion = 100000.0  # Umbral de reinversión en COP

# Calcular el interés y el monto final
intereses, monto_final = calcular_interes(capital_inicial, tasa_interes_anual, umbral_reinversion)

# Imprimir los resultados
print(f"Intereses generados: {intereses:.2f} COP")
print(f"Monto final en la cuenta: {monto_final:.2f} COP")
