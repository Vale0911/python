# Valores de entrada
x = (input("Ingrese el valor de x:"))
y = (input("Ingrese el valor de y:"))

# Inicialización de variables
a0, a1 = 1, 0
b0, b1 = 0, 1
x0, y0 = x, y

# Primer paso
q1 = x0 // y0 # q = cociente de la división
x1, y1 = y0, x0 - q1 * y0
a2, a3 = a1, a0 - q1 * a1
b2, b3 = b1, b0 - q1 * b1

# Segundo paso
if y1 != 0:
    q2 = x1 // y1
    x2, y2 = y1, x1 - q2 * y1
    a4, a5 = a3, a2 - q2 * a3
    b4, b5 = b3, b2 - q2 * b3

    # Tercer paso
    if y2 != 0:
        q3 = x2 // y2
        x3, y3 = y2, x2 - q3 * y2
        a6, a7 = a5, a4 - q3 * a5
        b6, b7 = b5, b4 - q3 * b5

        # Resultado final
        if y3 != 0:
            d = y3
            a = a7
            b = b7
        else:
            d = y2
            a = a5
            b = b5
    else:
        d = y1
        a = a3
        b = b3
else:
    d = y0
    a = a1
    b = b1

print("El MCD de {x} y {y} es {d}.")
print("Coeficientes a y b son: a = {a}, b = {b}.")
print("Esto satisface la ecuación: {a}*{x} + {b}*{y} = {d}")
