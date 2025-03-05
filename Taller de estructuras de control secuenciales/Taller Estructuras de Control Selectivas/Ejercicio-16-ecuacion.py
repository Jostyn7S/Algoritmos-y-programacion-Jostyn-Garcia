import math

def resolver_ecuacion_segundo_grado(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones son: X1 = {x1}, X2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"La solución única es: X1 = X2 = {x}"
    else:
        return "La ecuación no tiene solución en los números reales."

# Solicitar datos al usuario
a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))

# Verificar que A no sea cero
if a == 0:
    print("El coeficiente A no puede ser cero en una ecuación de segundo grado.")
else:
    resultado = resolver_ecuacion_segundo_grado(a, b, c)
    print(resultado)