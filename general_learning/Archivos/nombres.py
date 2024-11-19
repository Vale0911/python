# Crea un archivo de texto llamado nombres.txt que contenga una lista de nombres, cada uno en una línea diferente.
# El programa debe leer los nombres desde nombres.txt, ordenarlos alfabéticamente y luego escribir los nombres ordenados en un archivo llamado nombres_ordenados.txt.
# Leer nombres desde un archivo, ordenarlos y escribir en otro archivo

# Paso 1: Leer los nombres desde el archivo
with open('general_learning/Archivos/nombres.txt', 'r') as archivo:
    nombres = archivo.readlines()

# Paso 2: Limpiar los nombres (eliminar saltos de línea) y ordenarlos
nombres = [nombre.strip() for nombre in nombres]
nombres.sort()

# Paso 3: Escribir los nombres ordenados en un nuevo archivo
with open('nombres_ordenados.txt', 'w') as archivo_salida:
    for nombre in nombres:
        archivo_salida.write(nombre + '\n')

print("Los nombres han sido ordenados y guardados en 'nombres_ordenados.txt'.")