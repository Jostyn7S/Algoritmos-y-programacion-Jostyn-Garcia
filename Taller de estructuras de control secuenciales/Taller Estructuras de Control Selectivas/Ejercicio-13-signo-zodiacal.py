from datetime import datetime

def obtener_signo_zodiaco(dia, mes):
    signos = [
        (20, "Capricornio"), (19, "Acuario"), (20, "Piscis"), (20, "Aries"), (21, "Tauro"),
        (21, "Géminis"), (22, "Cáncer"), (23, "Leo"), (23, "Virgo"), (23, "Libra"),
        (22, "Escorpión"), (21, "Sagitario"), (22, "Capricornio")
    ]
    
    if dia > signos[mes - 1][0]:
        return signos[mes][1]
    else:
        return signos[mes - 1][1]

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Entrada del usuario
dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
año = int(input("Ingrese el año de nacimiento: "))

fecha_nacimiento = datetime(año, mes, dia)
signo = obtener_signo_zodiaco(dia, mes)
edad = calcular_edad(fecha_nacimiento)

print(f"Signo del zodiaco: {signo}")
print(f"Edad: {edad} años")
