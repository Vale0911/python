# Escribe una función sumar(a, b) que reciba dos números y devuelva su suma. Luego, llama a la función y muestra el resultado.
"""def sumar (a,b):
    return a+b
def aplicarOperacion (funcion, x,y):
    return funcion (x,y)
resultado = aplicarOperacion (sumar,10,5)
print ("Resultado:",resultado)"""
# Escribe una función es_par(n) que reciba un número y devuelva True si es par y False si es impar, Luego, usa esta función dentro de un ciclo for para mostrar si los números del 1 al 10 son pares o impares.
"""n = int(input("Ingrese el número del 0 al 10: "))

def es_par(n):
    return n % 2 == 0

for n in range (1,11):
    if es_par (n):
        print(f"{n} es un número par.")
    else:
        print(f"{n} es un número impar, no aplica.")"""
# Escribe una función aplicar_operacion(func, a, b) que reciba una función y dos números, y aplique la función a los números. Luego, pasa la función sumar como parámetro a esta función y muestra el resultado. 

"""def aplicar_operacion (func,a,b):
    return (func,a,b)
def sumar (x,y):
    return x+y
resultado = aplicar_operacion (sumar,20,1050)
print ("Resulatdo es:",resultado)"""
# Define una función factorial(n) que calcule el factorial de un número. Llama a la función y muestra el resultado para un número de tu elección.
def factorial (n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
            return 1
    else:
        resultado = 1
        for i in range (2,n+1):
            resultado *= i
        return resultado
numero = 5
resultado = factorial (numero)
print(f"El factorial de {numero} es {resultado}")