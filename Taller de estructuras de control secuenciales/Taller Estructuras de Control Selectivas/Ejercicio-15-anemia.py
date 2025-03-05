def determinar_anemia(edad, sexo, nivel_hemoglobina):
    if edad <= 1/12:
        rango_min, rango_max = 13, 26
    elif edad <= 6/12:
        rango_min, rango_max = 10, 18
    elif edad <= 12/12:
        rango_min, rango_max = 11, 15
    elif edad <= 5:
        rango_min, rango_max = 11.5, 15
    elif edad <= 10:
        rango_min, rango_max = 12.6, 15.5
    elif edad <= 15:
        rango_min, rango_max = 13, 15.5
    elif sexo.lower() == 'mujer':
        rango_min, rango_max = 12, 16
    elif sexo.lower() == 'hombre':
        rango_min, rango_max = 14, 18
    else:
        print("Error: Sexo no reconocido.")
        return
    
    resultado = "Positivo para anemia" if nivel_hemoglobina < rango_min else "Negativo para anemia"
    return resultado

# Solicitar datos al usuario
edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (hombre/mujer): ")
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

# Determinar y mostrar el resultado
resultado = determinar_anemia(edad, sexo, nivel_hemoglobina)
print(f"El resultado del análisis es: {resultado}")
