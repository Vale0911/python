import random

def generar_linea(linea, max_existencias, num_modelos):
    num_mod = 3 + random.randint(0, 7)
    for i in range(num_modelos):
        if i >= num_mod:
            linea[i] = -1
        else:
            linea[i] = 1 + random.randint(0, max_existencias)

def generar_lineas(linea0, linea1, linea2, max_existencias, num_modelos):
    generar_linea(linea0, max_existencias, num_modelos)
    generar_linea(linea1, max_existencias, num_modelos)
    generar_linea(linea2, max_existencias, num_modelos)

def generar_pedidos(codigos_pedido, cantidades_pedido, num_pedidos, max_num_cantidades):
    for i in range(num_pedidos):
        codigos_pedido[i] = int(input("Ingrese el número del modelo: "))
        while True:
            cantidades_pedido[i] = int(input("Ingrese la cantidad del modelo: "))
            if 0 <= cantidades_pedido[i] <= max_num_cantidades:
                break

def validar_pedido_ind(linea0, linea1, linea2, codigo, cant):
    linea = codigo // 100
    modelo = codigo % 100

    if linea > 2:
        print("Error - Línea no existe!")
        return False
    else:
        if linea == 0:
            if linea0[modelo] != -1 and linea0[modelo] >= cant:
                return True
        elif linea == 1:
            if linea1[modelo] != -1 and linea1[modelo] >= cant:
                return True
        elif linea == 2:
            if linea2[modelo] != -1 and linea2[modelo] >= cant:
                return True
    return False

def comprar_pedido_ind(linea0, linea1, linea2, codigo, cant):
    linea = codigo // 100
    modelo = codigo % 100

    if linea == 0:
        linea0[modelo] -= cant
    elif linea == 1:
        linea1[modelo] -= cant
    elif linea == 2:
        linea2[modelo] -= cant

def evaluar_pedido(linea0, linea1, linea2, codigos, cantidades, num_pedidos):
    viable = True
    for i in range(num_pedidos):
        viable = viable and validar_pedido_ind(linea0, linea1, linea2, codigos[i], cantidades[i])
    return viable

def comprar_pedido(linea0, linea1, linea2, codigos, cantidades, num_pedidos):
    for i in range(num_pedidos):
        comprar_pedido_ind(linea0, linea1, linea2, codigos[i], cantidades[i])

def mostrar_inventario_ind(num_linea, linea, max_num_modelos):
    i = 0
    while i < max_num_modelos and linea[i] != -1:
        print(f"({100 * num_linea + i},{linea[i]}) ", end="")
        i += 1
    print()

def mostrar_inventario(linea0, linea1, linea2, max_num_modelos):
    mostrar_inventario_ind(0, linea0, max_num_modelos)
    mostrar_inventario_ind(1, linea1, max_num_modelos)
    mostrar_inventario_ind(2, linea2, max_num_modelos)

def main():
    random.seed(1234)
    max_num_modelos = 10
    max_num_existencias = 20
    linea0 = [0] * max_num_modelos
    linea1 = [0] * max_num_modelos
    linea2 = [0] * max_num_modelos

    max_num_pedidos = 10
    max_num_cantidades = 5
    codigos_pedido = [0] * max_num_pedidos
    cantidades_pedido = [0] * max_num_pedidos

    generar_lineas(linea0, linea1, linea2, max_num_existencias, max_num_modelos)

    mostrar_inventario(linea0, linea1, linea2, max_num_modelos)

    num_pedidos = int(input("Escriba el número de modelos que quiere pedir: "))
    generar_pedidos(codigos_pedido, cantidades_pedido, num_pedidos, max_num_cantidades)

    if evaluar_pedido(linea0, linea1, linea2, codigos_pedido, cantidades_pedido, num_pedidos):
        comprar_pedido(linea0, linea1, linea2, codigos_pedido, cantidades_pedido, num_pedidos)
        print("¡Sí se pudo comprar el pedido!")
    else:
        print("¡No se pudo comprar el pedido!")

    mostrar_inventario(linea0, linea1, linea2, max_num_modelos)

if __name__ == "__main__":
    main()




