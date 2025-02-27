Algoritmo Ejercicio_21_Computador
	
	// Entradas
    Escribir "Ingrese el precio de compra al contado (P): "
    Leer P
    Escribir "Ingrese el valor de cada cuota mensual (T): "
    Leer T
	
    //Caja negra
    TotalCuotas <- T * 12
    Recargo <- TotalCuotas - P
    PorcentajeRecargo <- (Recargo / P) * 100
	
    //Salidas
    Escribir "Precio de contado: ", P, " COP"
    Escribir "Total a pagar por cuotas: ", TotalCuotas, " COP"
    Escribir "Recargo total: ", Recargo, " COP"
    Escribir "Porcentaje de recargo: ", PorcentajeRecargo, " %"
	
FinAlgoritmo
