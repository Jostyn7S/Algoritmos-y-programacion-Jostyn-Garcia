estudiantes = []
puntajes = []

while True:
    nombre = input("Ingrese el nombre del estudiante, o 'fin' para terminar: ")
    if nombre.lower() == 'fin':
        break
    
    try:
        puntaje = float(input(f"Ingrese el puntaje de {nombre}: "))
        if puntaje < 0:
            print("El puntaje no puede ser negativo. Intente nuevamente.")
            continue
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")
        continue
    
    estudiantes.append((nombre, puntaje))
    puntajes.append(puntaje)

if not estudiantes:
    print("No se ingresaron datos.")
else:
    max_puntaje = max(puntajes)
    min_puntaje = min(puntajes)
    promedio = sum(puntajes) / len(puntajes)
    
    estudiante_max = [nombre for nombre, puntaje in estudiantes if puntaje == max_puntaje]
    estudiante_min = [nombre for nombre, puntaje in estudiantes if puntaje == min_puntaje]
    
    inferiores_al_promedio = sum(1 for p in puntajes if p < promedio) / len(puntajes) * 100
    superiores_al_promedio = sum(1 for p in puntajes if p > promedio) / len(puntajes) * 100
    
    print("\nResultados:")
    print(f"Estudiante(s) con el puntaje más alto ({max_puntaje}): {', '.join(estudiante_max)}")
    print(f"Estudiante(s) con el puntaje más bajo ({min_puntaje}): {', '.join(estudiante_min)}")
    print(f"Puntaje máximo obtenido: {max_puntaje}")
    print(f"Puntaje mínimo obtenido: {min_puntaje}")
    print(f"Promedio de los puntajes: {promedio:.2f}")
    print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {inferiores_al_promedio:.2f}%")
    print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {superiores_al_promedio:.2f}%")