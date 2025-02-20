Algoritmo Ejercicio_15_Cantidad_descuento
	
	// Entradas
    Escribir "Ingrese el precio de venta al público (PVP): "
    Leer PVP
    Escribir "Ingrese el precio final pagado: "
    Leer PrecioFinal
	
	//Caja negra
    Descuento <- PVP - PrecioFinal
    PorcentajeDescuento <- (Descuento / PVP) * 100
	
    //Salidas
    Escribir "Descuento aplicado: ", Descuento, " COP"
    Escribir "Porcentaje de descuento: ", PorcentajeDescuento, " %"
	
FinAlgoritmo
