def CambioDivisas():
    
    # Definir variables
    Chelines = 0.0
    Dracmas = 0.0
    Pesetas = 0.0
    PesetasDesdeChelines = 0.0
    FrancosDesdeDracmas = 0.0
    DolaresDesdePesetas = 0.0
    LirasDesdePesetas = 0.0

    # Conversión de chelines austríacos a pesetas
    Chelines = float(input("Ingrese la cantidad en chelines austríacos: "))
    PesetasDesdeChelines = (Chelines * 956.871) / 100
    print(f"{Chelines} chelines austríacos equivalen a {PesetasDesdeChelines:.2f} pesetas.")

    # Conversión de dracmas griegos a francos franceses
    Dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
    FrancosDesdeDracmas = (Dracmas * 88.607) / 100 / 20.110
    print(f"{Dracmas} dracmas griegos equivalen a {FrancosDesdeDracmas:.2f} francos franceses.")

    # Conversión de pesetas a dólares estadounidenses y liras italianas
    Pesetas = float(input("Ingrese la cantidad en pesetas: "))
    DolaresDesdePesetas = Pesetas / 122.499
    LirasDesdePesetas = (Pesetas * 100) / 9.289
    print(f"{Pesetas} pesetas equivalen a {DolaresDesdePesetas:.2f} dólares estadounidenses.")
    print(f"{Pesetas} pesetas equivalen a {LirasDesdePesetas:.2f} liras italianas.")

CambioDivisas()