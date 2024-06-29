import cmath
# Solicitar datos al usuario
print('La ecuación cuadrática es: ax^2+bx+c=0')
a= float(input('Digite el coeficiente cuadrático a:'))
b= float(input('Digite el coeficiente lineal b:'))
c= float(input('Dgite el coeficiente independiente c:'))

# Calcular los puntos de corte
x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)

# Resultados
print('Las puntos de corte son:')
print('x1:', x1)
print('x2:', x2)
