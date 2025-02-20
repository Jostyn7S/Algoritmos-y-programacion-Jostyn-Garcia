Algoritmo  Ejercicio_3_Calcular_el_sueldo_del_vendedor
	
    //Entradas
    Escribir "Ingrese el sueldo base del vendedor: "
    Leer Sueldo_Base
	
    Escribir "Ingrese el monto de la primera venta: "
    Leer Venta1
    
    Escribir "Ingrese el monto de la segunda venta: "
    Leer Venta2
    
    Escribir "Ingrese el monto de la tercera venta: "
    Leer Venta3
	
    //Caja  negra
	Comisiones <- (Venta1 + Venta2 + Venta3) * 0.10
    Sueldo_Total <- Sueldo_Base + Comisiones
    
	//Salidas
    Escribir "El total de comisiones es: ", Comisiones
    Escribir "El sueldo total del vendedor es: ", Sueldo_Total
	
FinAlgoritmo
