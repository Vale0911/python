# Crea una función que reciba dos números, y modifique una variable global (como contador) para contar cuántas veces se llama la función.

# Definir una variable global contador
contador = 0

def contar_llamadas(num1, num2):
    global contador  # Indicar que queremos usar la variable global contador
    contador += 1   # Incrementar el contador
    # Aquí puedes realizar alguna operación con num1 y num2 si lo deseas
    print(f"Llamada número {contador}: num1 = {num1}, num2 = {num2}")

# Llamar a la función varias veces
contar_llamadas(5, 10)
contar_llamadas(3, 7)
contar_llamadas(1, 2)

# Mostrar el valor final del contador
print("La función fue llamada un total de", contador, "veces.")