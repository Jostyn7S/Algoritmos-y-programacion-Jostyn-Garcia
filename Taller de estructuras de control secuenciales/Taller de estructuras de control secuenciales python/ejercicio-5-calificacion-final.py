#Entradas
Parcial1=int(input("Ingrese la primera calificación parcial: "))
Parcial2=int(input("Ingrese la segunda calificación parcial: "))
Parcial3=int(input("Ingrese la tercera calificación parcial: "))
ExamenFinal=int(input("Ingrese la calificación del examen final: "))
TrabajoFinal=int(input("Ingrese la calificación del trabajo final: "))

#Caja negra
PromedioParciales=(Parcial1+Parcial2+Parcial3)/3
CalificacionFinal=(PromedioParciales*0.55)+(ExamenFinal*0.30)+(TrabajoFinal*0.15)

#Salida
print("La calificación final en computación es: ", CalificacionFinal)