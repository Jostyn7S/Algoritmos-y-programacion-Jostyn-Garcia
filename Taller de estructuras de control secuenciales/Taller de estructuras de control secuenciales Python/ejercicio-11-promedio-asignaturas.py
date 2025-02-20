def CalcularPromedios():
    # EntradaMatemática
    ExamenMat = float(input("Ingrese la nota del examen de Matemática: "))
    TareaMat1 = float(input("Ingrese la nota de la primera tarea de Matemática: "))
    TareaMat2 = float(input("Ingrese la nota de la segunda tarea de Matemática: "))
    TareaMat3 = float(input("Ingrese la nota de la tercera tarea de Matemática: "))

    # CálculoMatemática
    PromTareasMat = (TareaMat1 + TareaMat2 + TareaMat3) / 3
    PromedioMat = (ExamenMat * 0.90) + (PromTareasMat * 0.10)

    # EntradaFísica
    ExamenFis = float(input("Ingrese la nota del examen de Física: "))
    TareaFis1 = float(input("Ingrese la nota de la primera tarea de Física: "))
    TareaFis2 = float(input("Ingrese la nota de la segunda tarea de Física: "))

    # Cálculo del promedio de Física
    PromTareasFis = (TareaFis1 + TareaFis2) / 2
    PromedioFis = (ExamenFis * 0.80) + (PromTareasFis * 0.20)

    # Entrada de datos para Química
    ExamenQuim = float(input("Ingrese la nota del examen de Química: "))
    TareaQuim1 = float(input("Ingrese la nota de la primera tarea de Química: "))
    TareaQuim2 = float(input("Ingrese la nota de la segunda tarea de Química: "))
    TareaQuim3 = float(input("Ingrese la nota de la tercera tarea de Química: "))

    # Cálculo del promedio de Química
    PromTareasQuim = (TareaQuim1 + TareaQuim2 + TareaQuim3) / 3
    PromedioQuim = (ExamenQuim * 0.85) + (PromTareasQuim * 0.15)

    # Cálculo del promedio general
    PromedioGeneral = (PromedioMat + PromedioFis + PromedioQuim) / 3

    # Mostrar resultados
    print(f"Promedio en Matemática: {PromedioMat:.2f}")
    print(f"Promedio en Física: {PromedioFis:.2f}")
    print(f"Promedio en Química: {PromedioQuim:.2f}")
    print(f"Promedio general en las tres materias: {PromedioGeneral:.2f}")
    

CalcularPromedios()