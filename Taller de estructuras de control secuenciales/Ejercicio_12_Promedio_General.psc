Algoritmo Ejercicio_12_Promedio_General
	
	// Entrada de datos para Matem�tica
    Escribir "Ingrese la nota del examen de Matem�tica: "
    Leer ExamenMat
    Escribir "Ingrese la nota de la primera tarea de Matem�tica: "
    Leer TareaMat1
    Escribir "Ingrese la nota de la segunda tarea de Matem�tica: "
    Leer TareaMat2
    Escribir "Ingrese la nota de la tercera tarea de Matem�tica: "
    Leer TareaMat3
	
    // C�lculo del promedio de Matem�tica
    PromTareasMat <- (TareaMat1 + TareaMat2 + TareaMat3) / 3
    PromedioMat <- (ExamenMat * 0.90) + (PromTareasMat * 0.10)
	
    // Entrada de datos para F�sica
    Escribir "Ingrese la nota del examen de F�sica: "
    Leer ExamenFis
    Escribir "Ingrese la nota de la primera tarea de F�sica: "
    Leer TareaFis1
    Escribir "Ingrese la nota de la segunda tarea de F�sica: "
    Leer TareaFis2
	
    // C�lculo del promedio de F�sica
    PromTareasFis <- (TareaFis1 + TareaFis2) / 2
    PromedioFis <- (ExamenFis * 0.80) + (PromTareasFis * 0.20)
	
    // Entrada de datos para Qu�mica
    Escribir "Ingrese la nota del examen de Qu�mica: "
    Leer ExamenQuim
    Escribir "Ingrese la nota de la primera tarea de Qu�mica: "
    Leer TareaQuim1
    Escribir "Ingrese la nota de la segunda tarea de Qu�mica: "
    Leer TareaQuim2
    Escribir "Ingrese la nota de la tercera tarea de Qu�mica: "
    Leer TareaQuim3
	
    // C�lculo del promedio de Qu�mica
    PromTareasQuim <- (TareaQuim1 + TareaQuim2 + TareaQuim3) / 3
    PromedioQuim <- (ExamenQuim * 0.85) + (PromTareasQuim * 0.15)
	
    // C�lculo del promedio general
    PromedioGeneral <- (PromedioMat + PromedioFis + PromedioQuim) / 3
	
    // Mostrar resultados
    Escribir "--------------------------------------------------"
    Escribir "Promedio en Matem�tica: ", PromedioMat
    Escribir "Promedio en F�sica: ", PromedioFis
    Escribir "Promedio en Qu�mica: ", PromedioQuim
    Escribir "--------------------------------------------------"
    Escribir "Promedio general en las tres materias: ", PromedioGeneral
    Escribir "--------------------------------------------------"
	
FinAlgoritmo
