def CalcularSueldoTrabajador():
    
    # Definir variables
    Nombre = ""
    HorasNormales = 0.0
    HorasExtras = 0.0
    PagoHora = 0.0
    SueldoBase = 0.0
    PagoHorasExtras = 0.0
    SueldoBruto = 0.0
    DeduccionPagoForzoso = 0.0
    DeduccionPoliticaHabitacional = 0.0
    DeduccionCajaAhorro = 0.0
    TotalDeducciones = 0.0
    Hijos = 0
    AsignacionHijos = 0.0
    AsignacionAcademica = 250000
    AsignacionHogar = 180000
    TotalAsignaciones = 0.0
    SueldoNeto = 0.0
    # Entrada de datos
    Nombre = input("Ingrese el nombre del trabajador: ")
    HorasNormales = float(input("Ingrese el número de horas normales trabajadas: "))
    PagoHora = float(input("Ingrese el pago por una hora normal: "))
    HorasExtras = float(input("Ingrese el número de horas extras trabajadas: "))
    Hijos = int(input("Ingrese el número de hijos del trabajador: "))

    # Cálculo del sueldo base y horas extras
    SueldoBase = HorasNormales * PagoHora
    PagoHorasExtras = HorasExtras * (PagoHora * 1.25)
    SueldoBruto = SueldoBase + PagoHorasExtras

    # Cálculo de deducciones
    DeduccionPagoForzoso = SueldoBase * 0.05
    DeduccionPoliticaHabitacional = SueldoBase * 0.02
    DeduccionCajaAhorro = SueldoBase * 0.07
    TotalDeducciones = DeduccionPagoForzoso + DeduccionPoliticaHabitacional + DeduccionCajaAhorro

    # Cálculo de asignaciones
    AsignacionHijos = Hijos * 173000
    TotalAsignaciones = AsignacionAcademica + AsignacionHijos + AsignacionHogar

    # Cálculo del sueldo neto
    SueldoNeto = SueldoBruto - TotalDeducciones + TotalAsignaciones

    # Mostrar resultados
    print(f"Nombre del trabajador: {Nombre}")
    print(f"Sueldo base: {SueldoBase:.2f}")
    print(f"Pago por horas extras: {PagoHorasExtras:.2f}")
    print(f"Sueldo bruto: {SueldoBruto:.2f}")
    print("Deducciones:")
    print(f" - Pago forzoso (5%): {DeduccionPagoForzoso:.2f}")
    print(f" - Política habitacional (2%): {DeduccionPoliticaHabitacional:.2f}")
    print(f" - Caja de ahorro (7%): {DeduccionCajaAhorro:.2f}")
    print(f"Total de deducciones: {TotalDeducciones:.2f}")
    print("Asignaciones:")
    print(f" - Actualización académica: {AsignacionAcademica:.2f}")
    print(f" - Asignación por hijos: {AsignacionHijos:.2f}")
    print(f" - Prima por hogar: {AsignacionHogar:.2f}")
    print(f"Total de asignaciones: {TotalAsignaciones:.2f}")
    print(f"Sueldo neto a recibir: {SueldoNeto:.2f}")


CalcularSueldoTrabajador()