Algoritmo Ejercicio_10_Monedas
	
	// Conversión de chelines a pesetas
	//Entrada
    Escribir "Ingrese la cantidad en chelines austríacos: "
    Leer Chelines
	//Caja negra
    PesetasDesdeChelines <- (Chelines * 956.871) / 100
    //Salida
	Escribir Chelines, " chelines austríacos equivalen a ", PesetasDesdeChelines, " pesetas."
	
    // Conversión de dracmas a francos franceses
	//Entrada
    Escribir "Ingrese la cantidad en dracmas griegos: "
    Leer Dracmas
	//Caja  negra
    FrancosDesdeDracmas <- (Dracmas * 88.607) / 100 / 20.110
	//Salida
    Escribir Dracmas, " dracmas griegos equivalen a ", FrancosDesdeDracmas, " francos franceses."
	
    // Conversión de pesetas a dólares y liras italianas
	//Entrada
    Escribir "Ingrese la cantidad en pesetas: "
    Leer Pesetas
	//Caja negra
    DolaresDesdePesetas <- Pesetas / 122.499
    LirasDesdePesetas <- (Pesetas * 100) / 9.289
	//Salida
    Escribir Pesetas, " pesetas equivalen a ", DolaresDesdePesetas, " dólares estadounidenses."
    Escribir Pesetas, " pesetas equivalen a ", LirasDesdePesetas, " liras italianas."
	
FinAlgoritmo
