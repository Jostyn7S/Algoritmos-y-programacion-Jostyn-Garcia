Algoritmo Ejercicio_5_calificacion_final
	
	//Entradas
    Escribir "Ingrese la primera calificaci�n parcial: "
    Leer Parcial1
    
    Escribir "Ingrese la segunda calificaci�n parcial: "
    Leer Parcial2
    
    Escribir "Ingrese la tercera calificaci�n parcial: "
    Leer Parcial3
    
    Escribir "Ingrese la calificaci�n del examen final: "
    Leer Examen_Final
    
    Escribir "Ingrese la calificaci�n del trabajo final: "
    Leer Trabajo_Final
	
	//Caja negra
    Promedio_Parciales <- (Parcial1 + Parcial2 + Parcial3) / 3
    Calificacion_Final <- (Promedio_Parciales * 0.55) + (Examen_Final * 0.30) + (Trabajo_Final * 0.15)
	
	//Salida
    Escribir "La calificaci�n final en computaci�n es: ", Calificacion_Final
	
FinAlgoritmo
