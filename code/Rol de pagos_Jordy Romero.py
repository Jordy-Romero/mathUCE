# Función para calcular el sueldo
def calcular_sueldo():
    nombre = input("Ingrese el nombre de la persona: ")
    trabajo = input("Ingrese el trabajo de " + nombre + ": ")
    salario = float(input("Ingrese el salario de " + nombre + ": "))
    horas_extra = float(input("Ingrese el dinero de horas extra que trabajó " + nombre + ": "))
    fondos_reserva = float(input("Ingrese los fondos de reserva que ganó " + nombre + ": "))

    # Cálculo del total de ingresos
    total = salario + horas_extra + fondos_reserva
    # Cálculo del monto del IESS (9.45% del total)
    iees = total * 0.0945
    # Cálculo del subtotal después de deducir el IESS
    subtotal = total - iees
    # Cálculo del décimo tercero y décimo cuarto del salario
    decimo_tercero = subtotal / 12
    decimo_cuarto = subtotal / 12

    # Mostrar resultados
    print("Nombre:", nombre)
    print("Trabajo:", trabajo)
    print("Salario total sin descuentos:", total)
    print("Fondos de reserva:", fondos_reserva)
    print("IESS (9.45% del total):", iees)
    print("Subtotal:", subtotal)
    print("Decimo tercero:", decimo_tercero)
    print("Decimo cuarto:", decimo_cuarto)

# Llamar a la función para calcular el sueldo
calcular_sueldo()
