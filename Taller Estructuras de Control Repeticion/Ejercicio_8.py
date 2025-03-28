total_encuestados = 0
consumen_licor = 0
mujeres_menores = 0
hombres_sin_aguardiente = 0
suma_edades_cerveza = 0
cantidad_cerveza = 0
cantidad_whisky = 0

while True:
    consume = input("¿Consume licor? Si o No: ")
    if consume == 'Si' or consume == 'si':
        consumen_licor += 1
        licor = int(input("Licor preferido: 1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
    else:
        licor = 0
    
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    total_encuestados += 1
    
    if sexo == 'F' and edad < 18:
        mujeres_menores += 1
    
    if sexo == 'M' and 20 <= edad <= 25 and licor != 1:
        hombres_sin_aguardiente += 1
    
    if licor == 3:
        suma_edades_cerveza += edad
        cantidad_cerveza += 1
    
    if licor == 5:
        cantidad_whisky += 1
    
    continuar = input("¿Desea continuar? Si o No: ")
    if continuar != 'Si' and continuar != 'si':
        break

print("Resultados de la Encuesta:")
print(f"Total de personas que consumen licor: {consumen_licor}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {hombres_sin_aguardiente}")
if cantidad_cerveza > 0:
    print(f"Promedio de edad de quienes consumen cerveza: {suma_edades_cerveza / cantidad_cerveza:.2f}")
else:
    print("No hay consumidores de cerveza.")
if total_encuestados > 0:
    print(f"Porcentaje de personas que consumen whisky: {(cantidad_whisky / total_encuestados) * 100:.2f}%")
else:
    print("No hay encuestados.")