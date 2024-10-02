import random

# Función para calcular el estatus del pasajero
def obtener_estatus(codigo):
    if codigo % 12 == 0:
        return 'Diamante'
    elif codigo % 7 == 0:
        return 'VIP'
    else:
        return 'Normal'

# Función para calcular las millas de bonificación según el estatus
def calcular_millas(distancia, estatus):
    if estatus == 'Diamante':
        return distancia // 20
    elif estatus == 'VIP':
        return distancia // 60
    else:
        return distancia // 100

# Función para generar pasajeros
def generar_pasajeros(num_pasajeros):
    codigos = [random.randint(100, 999) for _ in range(num_pasajeros)]
    return codigos

# Función para generar la distancia de un vuelo
def generar_distancia():
    return random.randint(500, 5000)

# Función principal para la simulación de vuelos
def simular_vuelos(nv):
    if nv <= 0:
        print("El número de vuelos debe ser mayor que 0")
        return

    for vuelo in range(nv):
        print(f"\nVuelo {vuelo + 1}")
        num_pasajeros = random.randint(50, 100)
        distancia = generar_distancia()
        print(f"Distancia del vuelo: {distancia} km")
        codigos = generar_pasajeros(num_pasajeros)
        millas = [0] * num_pasajeros

        for i in range(num_pasajeros):
            estatus = obtener_estatus(codigos[i])
            bonificacion = calcular_millas(distancia, estatus)
            millas[i] += distancia + bonificacion
            print(f"Pasajero {codigos[i]} - {estatus} - Millas: {millas[i]}")

# Solicitar número de vuelos
nv = int(input("Ingrese el número de vuelos: "))
simular_vuelos(nv)
