#Entradas
Mujeres=int(input("Ingrese la cantidad de mujeres: "))
Hombres=int(input("Ingrese la cantidad de hombres: "))

#Caja negra 
TotalEstudiantes=(Mujeres+Hombres)
PorcentajeMujeres=(Mujeres/TotalEstudiantes*100)
PorcentajeHombres=(Hombres/TotalEstudiantes*100)

#Salida
print("El porcentaje de mujeres es de: ", PorcentajeMujeres, "%", "El porcentaje de hombres es de: ", PorcentajeHombres, "%")