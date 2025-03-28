conteo = 0
suma_puntajes = 0
max_puntaje = -1
min_puntaje = 101
nombre_max = ""
nombre_min = ""
inferiores = 0
superiores = 0

while True:
    nombre = input("Ingrese el nombre del estudiante, o 'fin' para terminar: ")
    if nombre == 'fin' or nombre == 'FIN' or nombre == 'Fin':
        break
    
    puntaje = input(f"Ingrese el puntaje de {nombre}: ")
    
    es_numero = False
    for caracter in puntaje:
        if caracter < '0' or caracter > '9':
            if caracter != '.' and caracter != '-':
                es_numero = True
                break
    
    if es_numero:
        print("Entrada inválida. Ingrese un número válido.")
        continue
    
    puntaje = float(puntaje)
    if puntaje < 0:
        print("El puntaje no puede ser negativo, Intente nuevamente")
        continue
    
    conteo += 1
    suma_puntajes += puntaje
    
    if puntaje > max_puntaje:
        max_puntaje = puntaje
        nombre_max = nombre
    elif puntaje == max_puntaje:
        nombre_max += ", " + nombre
    
    if puntaje < min_puntaje:
        min_puntaje = puntaje
        nombre_min = nombre
    elif puntaje == min_puntaje:
        nombre_min += ", " + nombre

if conteo == 0:
    print("No se ingresaron datos")
else:
    promedio = suma_puntajes / conteo
    
    contador = 0
    while contador < conteo:
        if puntaje < promedio:
            inferiores += 1
        elif puntaje > promedio:
            superiores += 1
        contador += 1
    
    porcentaje_inferiores = (inferiores / conteo) * 100
    porcentaje_superiores = (superiores / conteo) * 100
    
    print("\nResultados:")
    print(f"Estudiante con el puntaje mas alto ({max_puntaje}): {nombre_max}")
    print(f"Estudiante con el puntaje mas bajo ({min_puntaje}): {nombre_min}")
    print(f"Puntaje maximo obtenido: {max_puntaje}")
    print(f"Puntaje minimo obtenido: {min_puntaje}")
    print(f"Promedio de los puntajes: {promedio}")
    print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {porcentaje_inferiores}%")
    print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {porcentaje_superiores}%")
