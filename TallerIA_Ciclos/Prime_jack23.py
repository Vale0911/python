import random

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para lanzar dados
def lanzar_dados(cantidad=2):
    return [random.randint(1, 6) for _ in range(cantidad)]

# Función para jugar una ronda
def jugar_ronda():
    total = 0
    seguir_jugando = True

    while seguir_jugando and total < 23:
        dados = lanzar_dados()
        print(f"Lanzaste: {dados}")
        
        # Si el jugador saca dobles
        if dados[0] == dados[1]:
            print(f"¡Sacaste dobles de {dados[0]}!")
            # Permite dividir el lanzamiento
            for _ in range(2):  # Dos lanzamientos adicionales
                nuevos_dados = lanzar_dados(3)  # Se lanzan 3 dados
                print(f"Nuevos dados tras dividir: {nuevos_dados}")
                total += sum(nuevos_dados)
                if total >= 23:
                    seguir_jugando = False  # Detener si se pasa de 23
                if not seguir_jugando:
                    return total
            continue
        
        # Si el jugador saca 12
        if sum(dados) == 12:
            print("¡Sacaste un 12! Puedes lanzar un solo dado.")
            dado_extra = lanzar_dados(1)[0]
            print(f"Lanzaste el dado extra: {dado_extra}")
            total += dado_extra
            if total >= 23:
                seguir_jugando = False  # Detener si se alcanza 23
            continue

        total += sum(dados)

        print(f"Total acumulado: {total}")
        
        # Preguntar al jugador si desea seguir lanzando o quedarse con su total actual
        if total < 23:
            respuesta = input("¿Quieres lanzar de nuevo? (s/n): ").strip().lower()
            if respuesta != 's':
                seguir_jugando = False  # El jugador decide no seguir

    return total

# Función para determinar el ganador
def determinar_ganador(jugador1, jugador2):
    # Revisar si alguno tiene un número primo
    if es_primo(jugador1) and es_primo(jugador2):
        return 1 if jugador1 > jugador2 else 2
    if es_primo(jugador1):
        return 1
    if es_primo(jugador2):
        return 2
    
    # Si ninguno tiene primos, gana el que esté más cerca a 23
    return 1 if jugador1 <= 23 and (jugador1 > jugador2 or jugador2 > 23) else 2

# Juego principal
def juego_prime_jack():
    print("Turno del Jugador 1")
    jugador1 = jugar_ronda()
    print(f"Puntuación final del Jugador 1: {jugador1}\n")

    print("Turno del Jugador 2")
    jugador2 = jugar_ronda()
    print(f"Puntuación final del Jugador 2: {jugador2}\n")

    ganador = determinar_ganador(jugador1, jugador2)
    print(f"El ganador es el Jugador {ganador}")

# Ejecutar el juego
juego_prime_jack()




