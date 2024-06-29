Algoritmo ajustes
	Definir x,w,z,R Como Real
	Escribir 'Bienvenido al programa de ajustes'
	Escribir 'Solo se admiten valores para x, w, z en el rango (0,1)'
	Escribir 'Considerando que la fórmula es R=((8%*x/0.4%*w)+150%*z)^(0.2)'
	Escribir 'Digite el valor de x'
	Leer x
	Escribir 'Digite el valor de w'
	Leer w
	Escribir 'Digite el valor de z'
	Leer z
	R<-((0.08*x/(0.004*w))+(1.5*z))^0.2
	Escribir 'El resultado es: ',R
FinAlgoritmo