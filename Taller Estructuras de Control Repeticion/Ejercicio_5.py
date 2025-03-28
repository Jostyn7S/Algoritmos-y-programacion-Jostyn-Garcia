suma = 0
k = 1
contador = 0
while suma + ((k**2 + 1) / k) <= 1000:
    suma += (k**2 + 1) / k
    contador += 1
    k += 1
print(contador)