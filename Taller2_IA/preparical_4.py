import random

inventario = {
    0: {'modelo': 'Blusa A', 'existencias': 10},
    1: {'modelo': 'Blusa B', 'existencias': 15},
    2: {'modelo': 'Blusa C', 'existencias': 5},
    100: {'modelo': 'Falda A', 'existencias': 8},
    101: {'modelo': 'Falda B', 'existencias': 12},
    102: {'modelo': 'Falda C', 'existencias': 3},
    200: {'modelo': 'Jeans A', 'existencias': 7},
    201: {'modelo': 'Jeans B', 'existencias': 4},
    202: {'modelo': 'Jeans C', 'existencias': 10}
}

def mostrar_inventario():
    print("\nInventario actual:")
    for id_modelo, info in inventario.items():
        print(f"ID: {id_modelo}, Modelo: {info['modelo']}, Existencias: {info['existencias']}")

def procesar_pedido(pedido):
    for id_modelo, cantidad in pedido.items():
        if id_modelo not in inventario or inventario[id_modelo]['existencias'] < cantidad:
            return False, id_modelo
    for id_modelo, cantidad in pedido.items():
        inventario[id_modelo]['existencias'] -= cantidad
    return True, None

def realizar_compra():
    pedido = {}
    print("Ingrese su pedido (ID y cantidad). Ejemplo: 0 2 para 2 piezas del modelo con ID 0.")
    print("Escriba 'fin' para terminar el pedido.")

    continuar = True
    while continuar:
        entrada = input("ID y cantidad: ")
        if entrada.lower() == 'fin':
            continuar = False
            continue
        
        # Verificar que la entrada tenga el formato correcto
        partes = entrada.split()
        if len(partes) != 2:
            print("Entrada no válida. Por favor, use el formato 'ID cantidad'.")
            continue
        
        id_modelo = int(partes[0])
        cantidad = int(partes[1])

        if id_modelo in inventario and 1 <= cantidad <= 5:
            if id_modelo in pedido:
                pedido[id_modelo] += cantidad
            else:
                pedido[id_modelo] = cantidad
        else:
            print("ID de modelo no válido o cantidad fuera de rango (1-5).")

    if len(pedido) > 10:
        print("No se pueden pedir más de 10 modelos diferentes.")
        return

    exitoso, id_faltante = procesar_pedido(pedido)
    if exitoso:
        print("Compra exitosa. Detalle del pedido:")
        for id_modelo, cantidad in pedido.items():
            print(f"Modelo: {inventario[id_modelo]['modelo']}, Cantidad: {cantidad}")
    else:
        print(f"No se puede suplir el pedido, faltan existencias para el modelo con ID {id_faltante}.")

    mostrar_inventario()

if __name__ == "__main__":
    mostrar_inventario()
    realizar_compra()

