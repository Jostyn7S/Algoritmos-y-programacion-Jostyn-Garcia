Algoritmo Ejercicio_10_Monedas
	
	// Conversi�n de chelines a pesetas
	//Entrada
    Escribir "Ingrese la cantidad en chelines austr�acos: "
    Leer Chelines
	//Caja negra
    PesetasDesdeChelines <- (Chelines * 956.871) / 100
    //Salida
	Escribir Chelines, " chelines austr�acos equivalen a ", PesetasDesdeChelines, " pesetas."
	
    // Conversi�n de dracmas a francos franceses
	//Entrada
    Escribir "Ingrese la cantidad en dracmas griegos: "
    Leer Dracmas
	//Caja  negra
    FrancosDesdeDracmas <- (Dracmas * 88.607) / 100 / 20.110
	//Salida
    Escribir Dracmas, " dracmas griegos equivalen a ", FrancosDesdeDracmas, " francos franceses."
	
    // Conversi�n de pesetas a d�lares y liras italianas
	//Entrada
    Escribir "Ingrese la cantidad en pesetas: "
    Leer Pesetas
	//Caja negra
    DolaresDesdePesetas <- Pesetas / 122.499
    LirasDesdePesetas <- (Pesetas * 100) / 9.289
	//Salida
    Escribir Pesetas, " pesetas equivalen a ", DolaresDesdePesetas, " d�lares estadounidenses."
    Escribir Pesetas, " pesetas equivalen a ", LirasDesdePesetas, " liras italianas."
	
FinAlgoritmo
