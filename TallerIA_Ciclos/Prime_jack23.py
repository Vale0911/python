import random

random.seed(42)  # Semilla fija para los números aleatorios

# Número de jugadores
num_jugadores = int(input("Ingrese el número de jugadores: "))
jugadores = {}

# Ciclo para cada jugador
for i in range(1, num_jugadores + 1):
    print(f"\nTurno del Jugador {i}")

    # Lanzamiento de dos dados
    dados = [random.randint(1, 6) for _ in range(2)]
    suma = sum(dados)
    print(f"Lanzamiento inicial: {dados} -> Suma: {suma}")

    # Verifica si el número es primo
    es_primo = True
    if suma <= 1:
        es_primo = False
    for j in range(2, int(suma**0.5) + 1):
        if suma % j == 0:
            es_primo = False
            break

    # Si el jugador saca dobles
    if dados[0] == dados[1]:
        # Si sacó 12, puede lanzar 1 dado adicional
        if suma == 12:
            suma += random.randint(1, 6) - 6
        # Si sacó otros dobles, lanza 3 dados más
        else:
            suma = dados[0] + sum(random.randint(1, 6) for _ in range(3))

    jugadores[f"Jugador {i}"] = (suma, es_primo)

# Determinar el ganador: prioridad por números primos
ganador = None
max_puntaje = -1

for jugador, (puntaje, es_primo) in jugadores.items():
    if es_primo:
        if puntaje > max_puntaje:
            ganador = jugador
            max_puntaje = puntaje
    elif puntaje > max_puntaje:
        ganador = jugador
        max_puntaje = puntaje

print("El ganador es",ganador,"con un puntaje de: ", {jugadores[ganador][0]}.")

