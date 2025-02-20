Algoritmo Ejercicio_17_Presupuesto
	
	// Entradas
    Escribir "Ingrese el presupuesto total del hospital: "
    Leer PresupuestoTotal
	
    // Caja Negra
    Ginecologia <- PresupuestoTotal * 0.40
    Traumatologia <- PresupuestoTotal * 0.30
    Pediatria <- PresupuestoTotal * 0.30
	
    //Salidas
    Escribir "Presupuesto asignado a cada área:"
    Escribir "Ginecología: ", Ginecologia, " COP"
    Escribir "Traumatología: ", Traumatologia, " COP"
    Escribir "Pediatría: ", Pediatria, " COP"
	
FinAlgoritmo
