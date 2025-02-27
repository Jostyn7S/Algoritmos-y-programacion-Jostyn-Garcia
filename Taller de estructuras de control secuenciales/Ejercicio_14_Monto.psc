Algoritmo Ejercicio_14_Monto
	
	// Entradas
    Escribir "Ingrese la lectura anterior del medidor (kWh): "
    Leer lecturaAnterior
    Escribir "Ingrese la lectura actual del medidor (kWh): "
    Leer LecturaActual
    Escribir "Ingrese el costo por kilovatio (COP/kWh): "
    Leer CostoPorKilovatio
	
    //Caja negra
    Consumo <- LecturaActual - LecturaAnterior
    MontoTotal <- Consumo * CostoPorKilovatio
	
    //Salida
    Escribir "Consumo de energía en el mes: ", Consumo, " kWh"
    Escribir "Monto total a pagar: ", MontoTotal, " COP"
   
FinAlgoritmo
