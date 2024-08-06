import math

# Mostrar la fórmula cuadrática al usuario
print("La fórmula cuadrática es:")
print("x1 = (-b - sqrt(b^2 - 4ac)) / 2a")
print("x2 = (-b + sqrt(b^2 - 4ac)) / 2a")


# Pedir al usuario que ingrese los valores de a, b y c
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

xuno = (-b -(b**2 - 4*a*c))/(2*a)
xdos = (-b +(b**2 - 4*a*c)) / (2*a)

print("el valor de xuno es: ", xuno)
print("el valor de xdos es: ", xdos)