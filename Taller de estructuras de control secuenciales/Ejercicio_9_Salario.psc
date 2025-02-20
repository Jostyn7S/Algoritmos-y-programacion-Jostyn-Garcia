Algoritmo Ejercicio_9_Salario
	
	//Entradas
	Escribir "Ingrese el número de horas trabajadas: "
    Leer Horas_Trabajadas
	
    Escribir "Ingrese el precio por hora trabajada: "
    Leer Precio_Hora
	
	//Caja Negra
    Salario_Bruto <- Horas_Trabajadas * Precio_Hora
    Descuento <- Salario_Bruto * 0.20
    Salario_Neto <- Salario_Bruto - Descuento
	
	//Salidas
    Escribir "El salario bruto es: ", Salario_Bruto
    Escribir "El descuento por impuestos es: ", Descuento
    Escribir "El salario neto a recibir es: ", Salario_Neto
	
FinAlgoritmo
