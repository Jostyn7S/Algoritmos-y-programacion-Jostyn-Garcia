Algoritmo Ejercicio_12_Promedio_General
	
	// Entrada de datos para Matemática
    Escribir "Ingrese la nota del examen de Matemática: "
    Leer ExamenMat
    Escribir "Ingrese la nota de la primera tarea de Matemática: "
    Leer TareaMat1
    Escribir "Ingrese la nota de la segunda tarea de Matemática: "
    Leer TareaMat2
    Escribir "Ingrese la nota de la tercera tarea de Matemática: "
    Leer TareaMat3
	
    // Cálculo del promedio de Matemática
    PromTareasMat <- (TareaMat1 + TareaMat2 + TareaMat3) / 3
    PromedioMat <- (ExamenMat * 0.90) + (PromTareasMat * 0.10)
	
    // Entrada de datos para Física
    Escribir "Ingrese la nota del examen de Física: "
    Leer ExamenFis
    Escribir "Ingrese la nota de la primera tarea de Física: "
    Leer TareaFis1
    Escribir "Ingrese la nota de la segunda tarea de Física: "
    Leer TareaFis2
	
    // Cálculo del promedio de Física
    PromTareasFis <- (TareaFis1 + TareaFis2) / 2
    PromedioFis <- (ExamenFis * 0.80) + (PromTareasFis * 0.20)
	
    // Entrada de datos para Química
    Escribir "Ingrese la nota del examen de Química: "
    Leer ExamenQuim
    Escribir "Ingrese la nota de la primera tarea de Química: "
    Leer TareaQuim1
    Escribir "Ingrese la nota de la segunda tarea de Química: "
    Leer TareaQuim2
    Escribir "Ingrese la nota de la tercera tarea de Química: "
    Leer TareaQuim3
	
    // Cálculo del promedio de Química
    PromTareasQuim <- (TareaQuim1 + TareaQuim2 + TareaQuim3) / 3
    PromedioQuim <- (ExamenQuim * 0.85) + (PromTareasQuim * 0.15)
	
    // Cálculo del promedio general
    PromedioGeneral <- (PromedioMat + PromedioFis + PromedioQuim) / 3
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Promedio en Matemática: ", PromedioMat
    Escribir "Promedio en Física: ", PromedioFis
    Escribir "Promedio en Química: ", PromedioQuim
    Escribir "--------------------------------------------------"
    Escribir "Promedio general en las tres materias: ", PromedioGeneral
    Escribir "--------------------------------------------------"
	
FinAlgoritmo
