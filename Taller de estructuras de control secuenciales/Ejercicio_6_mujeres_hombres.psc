Algoritmo Ejercicio_6_mujeres_hombres
	
	//Entradas
	Escribir "Ingrese el numero de mujeres " 
	Leer Mujeres
	Escribir "Ingrese el numero de hombres "
	Leer Hombres
	
	//Caja negra
	Total_Estudiantes<-Mujeres+Hombres
	porMujeres<-(Mujeres/Total_Estudiantes*100)
	porHombres<-(Hombres/Total_Estudiantes*100)
	
	//Salidas
	Escribir "El porcentaje de hombres es de ", porHombres, "%"
	Escribir "El porcentaje de mujeres es de ", porMujeres, "%"
FinAlgoritmo
