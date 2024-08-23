import math

x = float(input("Ingrese el valor de x:"))
y = float(input("ingrese el valor de y:"))

parte_uno = math.sqrt(5*x + (math.sqrt(y**(x-1)))/(y+2*x))**3
parte_dos = ((x**2)**3)/((y**3)*x+1)
parte_tres = 3*(math.sqrt(3+math.sqrt(x-1)))
z = parte_uno-(parte_dos-parte_tres)
print(z)