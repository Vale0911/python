import math

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))


parte1 = math.sqrt((2 * x + y**2) / (3 + x))
parte2 = (x**2 / (y**3 + x)) - 5 * math.sqrt(3 * x)

z = parte1 - parte2

print("El valor de z es:", z)

