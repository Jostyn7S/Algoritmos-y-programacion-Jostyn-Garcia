n = int(input())

suma = 0
for i in range(1, n):
    if n % i == 0:
        suma += i

if suma == n:
    print(n, "es un número perfecto.")
else:
    print(n, "no es un número perfecto.")
