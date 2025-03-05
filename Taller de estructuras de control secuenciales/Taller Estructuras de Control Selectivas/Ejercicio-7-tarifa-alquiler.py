def calcular_pago(distancia):
    if distancia <= 300:
        costo = 50000
    elif distancia <= 1000:
        costo = 70000 + (distancia - 300) * 30000
    else:
        costo = 150000 + (distancia - 1000) * 9000
    
    return costo

# Ejemplo de uso
distancia = float(input("Ingrese la distancia recorrida en km: "))
costo_total = calcular_pago(distancia)
print(f"El total a pagar es: ${costo_total:,.2f} COP")
