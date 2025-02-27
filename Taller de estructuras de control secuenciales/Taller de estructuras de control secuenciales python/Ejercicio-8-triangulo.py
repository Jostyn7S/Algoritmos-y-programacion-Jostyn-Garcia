#Entradas
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

#Caja negra
s = (a + b + c) / 2
Area = (s * (s - a) * (s - b) * (s - c))

#Salida
print("El área del triángulo es: " , Area)