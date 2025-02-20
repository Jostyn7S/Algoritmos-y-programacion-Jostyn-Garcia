Algoritmo Ejercicio_11_Promedio_Sueldo
	
    // Entrada de datos
    Escribir "Ingrese el nombre del trabajador: "
    Leer Nombre
	
    Escribir "Ingrese el número de horas normales trabajadas: "
    Leer HorasNormales
	
    Escribir "Ingrese el pago por una hora normal: "
    Leer PagoHora
	
    Escribir "Ingrese el número de horas extras trabajadas: "
    Leer HorasExtras
	
    Escribir "Ingrese el número de hijos del trabajador: "
    Leer Hijos
	
    // Cálculo del sueldo base y horas extras
    SueldoBase <- HorasNormales * PagoHora
    PagoHorasExtras <- HorasExtras * (PagoHora * 1.25)
    SueldoBruto <- SueldoBase + PagoHorasExtras
	
    // Cálculo de deducciones
    DeduccionPagoForzoso <- SueldoBase * 0.05
    DeduccionPoliticaHabitacional <- SueldoBase * 0.02
    DeduccionCajaAhorro <- SueldoBase * 0.07
    TotalDeducciones <- DeduccionPagoForzoso + DeduccionPoliticaHabitacional + DeduccionCajaAhorro
	
    // Cálculo de asignaciones
    AsignacionAcademica <- 250000
    AsignacionHijos <- Hijos * 173000
    AsignacionHogar <- 180000
    TotalAsignaciones <- AsignacionAcademica + AsignacionHijos + AsignacionHogar
	
    // Cálculo del sueldo neto
    SueldoNeto <- SueldoBruto - TotalDeducciones + TotalAsignaciones
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Nombre del trabajador: ", Nombre
    Escribir "Sueldo base: ", SueldoBase
    Escribir "Pago por horas extras: ", PagoHorasExtras
    Escribir "Sueldo bruto: ", SueldoBruto
    Escribir "--------------------------------------------------"
    Escribir "Deducciones:"
    Escribir " - Pago forzoso (5%): ", DeduccionPagoForzoso
    Escribir " - Política habitacional (2%): ", DeduccionPoliticaHabitacional
    Escribir " - Caja de ahorro (7%): ", DeduccionCajaAhorro
    Escribir "Total de deducciones: ", TotalDeducciones
    Escribir "--------------------------------------------------"
    Escribir "Asignaciones:"
    Escribir " - Actualización académica: ", AsignacionAcademica
    Escribir " - Asignación por hijos: ", AsignacionHijos
    Escribir " - Prima por hogar: ", AsignacionHogar
    Escribir "Total de asignaciones: ", TotalAsignaciones
    Escribir "--------------------------------------------------"
    Escribir "Sueldo neto a recibir: ", SueldoNeto
    Escribir "--------------------------------------------------"
	
FinAlgoritmo
