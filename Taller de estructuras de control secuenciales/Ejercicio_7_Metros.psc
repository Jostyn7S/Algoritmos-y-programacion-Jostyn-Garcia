Algoritmo Ejercicio_7_Metros
	
	//Entrada
    Escribir "Ingrese la cantidad en metros: "
    Leer Metros
	
	//Caja negra
    Pulgadas_Totales <- Metros * 39.27
    Pies <- trunc(Pulgadas_Totales / 12)
    Pulgadas_Restantes <- Pulgadas_Totales - (Pies * 12)
	
	//Salida
    Escribir "Equivalencia: ", Pies, " pies y ", Pulgadas_Restantes, " pulgadas."
	
FinAlgoritmo
