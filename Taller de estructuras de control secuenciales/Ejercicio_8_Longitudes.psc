Algoritmo Ejercicio_8_Longitudes
	
	//Entradas
		Escribir "Ingrese la longitud del lado a: "
		Leer a
		
		Escribir "Ingrese la longitud del lado b: "
		Leer b
		
		Escribir "Ingrese la longitud del lado c: "
		Leer c
		
		//Caja negra
		s <- (a + b + c) / 2
		Area <- raiz(s * (s - a) * (s - b) * (s - c))
		
		//Salida
		Escribir "El área del triángulo es: ", Area
		
FinAlgoritmo
