Algoritmo Ejercicio_19_Naranjas
	
	// Entradas
    Escribir "Ingrese la cantidad de naranjas compradas (X): "
    Leer X
    Escribir "Ingrese el costo por docena de naranjas (Bs): "
    Leer u
    Escribir "Ingrese el total obtenido por la venta de las naranjas (Bs): "
    Leer K
	
    //Caja negra
    CostoTotal <- (X / 12) * u
    Ganancia <- K - CostoTotal
	PorcentajeGanancia <- (Ganancia / CostoTotal) * 100
	
    //Salidas
    Escribir "Costo total de la compra: ", CostoTotal, " Bs"
    Escribir "Ganancia obtenida: ", Ganancia, " Bs"
    Escribir "Porcentaje de ganancia: ", PorcentajeGanancia, " %"
	
FinAlgoritmo
