def desglosar_cantidad(cantidad):
    billetes_monedas = [
        100000, 50000, 20000, 10000, 5000, 2000, 1000,
        500, 200, 100, 50
    ]
    
    cantidad = cantidad - (cantidad % 50)  # Eliminar unidades
    desglose = []
    
    for valor in billetes_monedas:
        if cantidad >= valor:
            conteo = cantidad // valor
            cantidad %= valor
            desglose.extend([valor] * conteo)
    
    print("Desglose:", ", ".join(map(str, desglose)))

# Ejemplo de uso
cantidad = int(input("Ingrese la cantidad en COP: "))
desglosar_cantidad(cantidad)
