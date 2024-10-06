import random

def generar_lineas(linea0, linea1, linea2, max_num_existencias, max_num_modelos):
    for i in range(max_num_modelos):
        linea0[i] = random.randint(0, max_num_existencias)
        linea1[i] = random.randint(0, max_num_existencias)
        linea2[i] = random.randint(0, max_num_existencias)

def mostrar_inventario(linea0, linea1, linea2, max_num_modelos):
    for i in range(max_num_modelos):
        print(f"Modelo {i}: Linea0 - {linea0[i]}, Linea1 - {linea1[i]}, Linea2 - {linea2[i]}")

def generar_pedidos(num_pedidos, max_num_modelos):
    codigos_pedido = []
    cantidades_pedido = []
    
    for _ in range(num_pedidos):
    
        codigo = int(input(f"Ingrese el código del modelo a pedir (0-{max_num_modelos-1}): "))
        
        while codigo < 0 or codigo >= max_num_modelos:
            print(f"Error: el código debe estar entre 0 y {max_num_modelos-1}.")
            codigo = int(input(f"Ingrese el código del modelo a pedir (0-{max_num_modelos-1}): "))
        
        cantidad = int(input("Ingrese la cantidad a pedir: "))
        
        codigos_pedido.append(codigo)
        cantidades_pedido.append(cantidad)
    
    return codigos_pedido, cantidades_pedido

def evaluar_pedido(linea0, linea1, linea2, codigos_pedido, cantidades_pedido):
    for codigo, cantidad in zip(codigos_pedido, cantidades_pedido):
        if cantidad > linea0[codigo] or cantidad > linea1[codigo] or cantidad > linea2[codigo]:
            print(f"El modelo {codigo} no tiene suficientes existencias.")
            return False
    return True

def main():
    max_num_existencias = 20
    max_num_modelos = 10

    linea0 = [0] * max_num_modelos
    linea1 = [0] * max_num_modelos
    linea2 = [0] * max_num_modelos

    generar_lineas(linea0, linea1, linea2, max_num_existencias, max_num_modelos)
    
    mostrar_inventario(linea0, linea1, linea2, max_num_modelos)

    num_pedidos = int(input("Escriba el número de modelos que quiere pedir: "))
    
    codigos_pedido, cantidades_pedido = generar_pedidos(num_pedidos, max_num_modelos)

    if evaluar_pedido(linea0, linea1, linea2, codigos_pedido, cantidades_pedido):
        print("El pedido puede ser cumplido.")
    else:
        print("El pedido no puede ser cumplido.")

    mostrar_inventario(linea0, linea1, linea2, max_num_modelos)

if __name__ == "__main__":
    main()



