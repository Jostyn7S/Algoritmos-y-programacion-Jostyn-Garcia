Algoritmo Ejercicio_9
	
    Escribir "Ingrese el número: "
    Leer numero1
	
    numero2 <- numero1
    reverso <- 0
	
    Mientras numero1 > 0 Hacer
        digito <- numero1 mod 10
        reverso <- (reverso * 10) + digito
        numero1 <- Trunc (numero1 / 10)
    Fin Mientras
	
    Si numero2 = reverso Entonces
        Escribir "Es un palíndromo"
    SiNo
        Escribir "No es un palíndromo"
    Fin Si
	
FinAlgoritmo
