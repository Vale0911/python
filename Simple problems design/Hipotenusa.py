import math 
print("Hallando la hipotenusa de un triángulo rectángulo")

#pedir al usuario que ingrese los valores de los catetos
cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

#calcular la hipotenusa utilizando la fórmula de la hipotenusa
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

#mostrar el resultado al usuario
print("La hipotenusa del triángulo es: ", hipotenusa)

#mostrar la fórmula utilizada
print("La fórmula utilizada es: sqrt((cateto1^2) + (cateto2^2))")