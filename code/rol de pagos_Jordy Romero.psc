Proceso Calculoderoldepago
	Definir nombre, trabajo como Cadena
    Definir salario, horas_extra, fondos_reserva, iees, subtotal, decimo_tercero, decimo_cuarto, total como Real
	
    Escribir "Ingrese el nombre de la persona:"
    Leer nombre
    Escribir "Ingrese el trabajo de", nombre, ":"
    Leer trabajo
    Escribir "Ingrese el salario de", nombre, ":"
    Leer salario
    Escribir "Ingrese el dinero de horas extra que trabajó", nombre, ":"
    Leer horas_extra
    Escribir "Ingrese los fondos de reserva que ganó", nombre, ":"
    Leer fondos_reserva
	
    total <- salario + horas_extra + fondos_reserva
    iees <- total * 0.0945
    subtotal <- total - iees
	
    decimo_tercero <- subtotal / 12
    decimo_cuarto <- subtotal / 12
	
    Escribir "Nombre:", nombre
    Escribir "Trabajo:", trabajo
    Escribir "Salario total sin descuentos:", total
    Escribir "Fondos de reserva:", fondos_reserva
    Escribir "IEES (9.45% del total):", iees
    Escribir "Subtotal:", subtotal
    Escribir "Decimo tercero:", decimo_tercero
    Escribir "Decimo cuarto:", decimo_cuarto

FinProceso
