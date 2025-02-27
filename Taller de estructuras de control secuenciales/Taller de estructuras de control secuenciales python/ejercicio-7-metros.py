def ConvertirMetrosaPiesPulgadas():
    Metros = float(input("Ingrese la cantidad en metros: "))
    PulgadasPorMetro = 39.27
    PiesPorPulgada = 1 / 12

    Pulgadas = Metros * PulgadasPorMetro
    
    Pies = int(Pulgadas // 12)
    PulgadasRestantes = Pulgadas % 12

    print(f"{Metros} metros son equivalentes a {Pies} pies y {PulgadasRestantes:.2f} pulgadas.")

ConvertirMetrosaPiesPulgadas()