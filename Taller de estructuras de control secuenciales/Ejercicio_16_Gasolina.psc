Algoritmo Ejercicio_16_Gasolina
	
	// Definir la conversión de galones a litros
    LitrosPorGalon <- 3.785
    PrecioPorLitro <- 50000  // Precio del litro de gasolina en COP
	
    // Entrada
    Escribir "Ingrese la cantidad de galones surtidos: "
    Leer Galones
	
    //Caja Negra
	Litros <- Galones * LitrosPorGalon
    TotalPagar <- Litros * PrecioPorLitro
	
    //Salidas
    Escribir "Cantidad de litros surtidos: ", Litros, " L"
    Escribir "Total a pagar: ", TotalPagar, " COP"
	
FinAlgoritmo
