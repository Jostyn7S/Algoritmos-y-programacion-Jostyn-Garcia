def verificar_expresion(P, Q):
    expresion = (P**3) + (Q**4) - (2 * P**2)
    if expresion > 680:
        print(f"P = {P} y Q = {Q} satisfacen la expresión.")
    else:
        print(f"P = {P} y Q = {Q} no satisfacen la expresión.")

# Ejemplo de uso
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))
verificar_expresion(P, Q)
