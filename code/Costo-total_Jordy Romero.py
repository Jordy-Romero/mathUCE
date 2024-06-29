print("Ingrese el largo en metros")
largo = float(input())
print("Ingrese el ancho en metros")
ancho = float(input())
area = largo * ancho
numero_baldosas = area / 0.003
costo_total=numero_baldosas * 3.5
print("El área es:",area, "metros cuadrados")
print("El número de baldosas a utilizar es:", numero_baldosas)
print("El costo total es:", costo_total, "USD")
print("Gracias por usar nuestro porgrama. Vuelva pronto.")
