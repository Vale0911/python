import random

modelos = ['Blusa A', 'Blusa B', 'Blusa C', 'Falda A', 'Falda B', 'Falda C', 'Jeans A', 'Jeans B', 'Jeans C']
existencias = [10, 15, 5, 8, 12, 3, 7, 4, 10]

def mostrar_inventario():
    print("\nInventario actual:")
    for i in range(len(modelos)):
        print(f"ID: {i}, Modelo: {modelos[i]}, Existencias: {existencias[i]}")

def procesar_pedido(pedido):
    for id_modelo, cantidad in pedido:
        if id_modelo < 0 or id_modelo >= len(modelos) or existencias[id_modelo] < cantidad:
            return False, id_modelo
    for id_modelo, cantidad in pedido:
        existencias[id_modelo] -= cantidad
    return True, None

def realizar_compra():
    pedido = []
    print("Ingrese su pedido (ID y cantidad). Ejemplo: 0 2 para 2 piezas del modelo con ID 0.")
    print("Escriba 'fin' para terminar el pedido.")

    while True:
        entrada = input("ID y cantidad: ")
        if entrada.lower() == 'fin':
            break
        
        # Verificar que la entrada tenga el formato correcto
        partes = entrada.split()
        if len(partes) != 2:
            print("Entrada no válida. Por favor, use el formato 'ID cantidad'.")
            continue
        
        id_modelo = int(partes[0])
        cantidad = int(partes[1])

        if 0 <= id_modelo < len(modelos) and 1 <= cantidad <= 5:
            # Verificar si el modelo ya está en el pedido
            for i in range(len(pedido)):
                if pedido[i][0] == id_modelo:
                    pedido[i][1] += cantidad
                    break
            else:
                pedido.append([id_modelo, cantidad])
        else:
            print("ID de modelo no válido o cantidad fuera de rango (1-5).")

    if len(pedido) > 10:
        print("No se pueden pedir más de 10 modelos diferentes.")
        return

    exitoso, id_faltante = procesar_pedido(pedido)
    if exitoso:
        print("Compra exitosa. Detalle del pedido:")
        for id_modelo, cantidad in pedido:
            print(f"Modelo: {modelos[id_modelo]}, Cantidad: {cantidad}")
    else:
        print(f"No se puede suplir el pedido, faltan existencias para el modelo con ID {id_faltante}.")

    mostrar_inventario()

if __name__ == "__main__":
    mostrar_inventario()
    realizar_compra()

