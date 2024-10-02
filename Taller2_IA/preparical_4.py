def generar_lineas(linea0, linea1, linea2, max_num_existencias, max_num_modelos):
 


def mostrar_inventario(linea0, linea1, linea2, max_num_modelos):

    for i in range(max_num_modelos):
        print(f"Modelo {i}: Linea0 - {linea0[i]}, Linea1 - {linea1[i]}, Linea2 - {linea2[i]}")

def generar_pedidos(num_pedidos):
    codigos_pedido = []
    cantidades_pedido = []
    
    for _ in range(num_pedidos):
        codigo = int(input("Ingrese el código del modelo a pedir: "))
        cantidad = int(input("Ingrese la cantidad a pedir: "))
        
        codigos_pedido.append(codigo)
        cantidades_pedido.append(cantidad)
    
    return codigos_pedido, cantidades_pedido

def evaluar_pedido(linea0, linea1, linea2, codigos_pedido, cantidades_pedido):
    for codigo, cantidad in zip(codigos_pedido, cantidades_pedido):
        if codigo < len(linea0):
            # Comprobar si hay suficiente stock
            if cantidad > linea0[codigo]:
                return False
    return True

def main():
    max_num_existencias = 100
    max_num_modelos = 50
    max_num_cantidades = 100

    linea0 = [0] * max_num_modelos
    linea1 = [0] * max_num_modelos
    linea2 = [0] * max_num_modelos

    generar_lineas(linea0, linea1, linea2, max_num_existencias, max_num_modelos)
    
    mostrar_inventario(linea0, linea1, linea2, max_num_modelos)

    num_pedidos = int(input("Escriba el número de modelos que quiere pedir: "))
    
    codigos_pedido, cantidades_pedido = generar_pedidos(num_pedidos)

    if evaluar_pedido(linea0, linea1, linea2, codigos_pedido, cantidades_pedido):
        print("El pedido puede ser cumplido.")
    else:
        print("El pedido no puede ser cumplido.")

if __name__ == "__main__":
    main()

    mostrar_inventario()
    realizar_compra()

