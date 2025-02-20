Algoritmo Ejercicio_18_Interes_Bolivares
	
	// Entradas
    Escribir "Ingrese el capital prestado (Bolívares): "
    Leer Capital
    Escribir "Ingrese el total de intereses pagados (Bolívares): "
    Leer InteresPagado
    Tiempo <- 4  // Se establece el tiempo fijo en 4 años
	
    // Caja negra
    TasaInteres <- (InteresPagado * 100) / (Capital * Tiempo)
	
    //Salida
    Escribir "La tasa de interés anual cobrada es: ", TasaInteres, " %"
	
FinAlgoritmo
