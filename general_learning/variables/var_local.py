# Define una variable global x = 10 y luego, dentro de una función, cambia el valor de x y muestra el valor dentro de la función y fuera de ella.
x = 10 
def cambiar_valor():
    global x
    x = 20
    print("Dentro de la función, x =",x)
cambiar_valor()
print("Fuera de la función, x =",x)  
