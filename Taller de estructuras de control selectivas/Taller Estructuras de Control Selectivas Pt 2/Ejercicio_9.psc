Algoritmo Ejercicio_9
	
    Escribir "Ingrese el n�mero: "
    Leer numero1
	
    numero2 <- numero1
    reverso <- 0
	
    Mientras numero1 > 0 Hacer
        digito <- numero1 mod 10
        reverso <- (reverso * 10) + digito
        numero1 <- Trunc (numero1 / 10)
    Fin Mientras
	
    Si numero2 = reverso Entonces
        Escribir "Es un pal�ndromo"
    SiNo
        Escribir "No es un pal�ndromo"
    Fin Si
	
FinAlgoritmo
