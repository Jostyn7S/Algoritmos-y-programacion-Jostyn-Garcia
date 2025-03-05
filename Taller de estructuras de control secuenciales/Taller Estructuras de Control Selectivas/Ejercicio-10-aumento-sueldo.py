def calcular_nuevo_sueldo(categoria, sueldo_bruto):
    aumentos = {
        1: 0.10,
        2: 0.15,
        3: 0.20,
        4: 0.40,
        5: 0.60
    }
    
    if categoria in aumentos:
        aumento = sueldo_bruto * aumentos[categoria]
        nuevo_sueldo = sueldo_bruto + aumento
        print(f"Categoría del trabajador: {categoria}")
        print(f"Nuevo sueldo bruto: ${nuevo_sueldo:,.2f} COP")
    else:
        print("Categoría no válida.")

# Ejemplo de uso
categoria = int(input("Ingrese la categoría del trabajador (1-5): "))
sueldo_bruto = float(input("Ingrese el sueldo bruto en COP: "))
calcular_nuevo_sueldo(categoria, sueldo_bruto)