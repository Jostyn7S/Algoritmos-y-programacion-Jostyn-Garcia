Algoritmo Ejercicio_18_Interes_Bolivares
	
	// Entradas
    Escribir "Ingrese el capital prestado (Bol�vares): "
    Leer Capital
    Escribir "Ingrese el total de intereses pagados (Bol�vares): "
    Leer InteresPagado
    Tiempo <- 4  // Se establece el tiempo fijo en 4 a�os
	
    // Caja negra
    TasaInteres <- (InteresPagado * 100) / (Capital * Tiempo)
	
    //Salida
    Escribir "La tasa de inter�s anual cobrada es: ", TasaInteres, " %"
	
FinAlgoritmo
