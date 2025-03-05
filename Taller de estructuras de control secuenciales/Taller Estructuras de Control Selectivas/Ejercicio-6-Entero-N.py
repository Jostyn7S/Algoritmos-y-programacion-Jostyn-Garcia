def redondear_a_centena(A, B, C, D):
    N = A * 1000 + B * 100 + C * 10 + D
    redondeado = round(N, -2)
    return redondeado

# Ejemplo de uso
A = int(input("Ingrese el dígito A: "))
B = int(input("Ingrese el dígito B: "))
C = int(input("Ingrese el dígito C: "))
D = int(input("Ingrese el dígito D: "))

resultado = redondear_a_centena(A, B, C, D)
print(f"El número redondeado a la centena más próxima es: {resultado}")
