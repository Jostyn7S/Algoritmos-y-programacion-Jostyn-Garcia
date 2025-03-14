Algoritmo Ejercicio_7
	Escribir "Ingrese el número: "
	Leer numero1
	Si numero1 > 1 Entonces
		S <- 0
		Para i Desde 1 Hasta numero1 Hacer
			Si numero1 mod i = 0 Entonces
				S <- S + 1
			Fin Si
		Fin Para
		Si S = 2 Entonces
			Escribir "Es primo"
		SiNo
			Escribir "No es primo"
		Fin Si
	SiNo
		Escribir "No es primo"
	Fin Si
FinAlgoritmo
