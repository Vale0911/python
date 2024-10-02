import random

# Función para generar partidos
def generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos):
    partido = 0
    for i in range(num_equipos):
        for j in range(num_equipos):
            if i != j:  # Los equipos no pueden jugar contra sí mismos
                equipo_local[partido] = i
                equipo_visita[partido] = j
                goles_local[partido] = random.randint(0, 5)  # Goles aleatorios entre 0 y 5
                goles_visita[partido] = random.randint(0, 5)
                partido += 1

# Función para calcular puntos
def calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, total_puntos, num_partidos):
    for partido in range(num_partidos):
        if goles_local[partido] > goles_visita[partido]:
            total_puntos[equipo_local[partido]] += 3  # Gana el equipo local
        elif goles_local[partido] < goles_visita[partido]:
            total_puntos[equipo_visita[partido]] += 3  # Gana el equipo visitante
        else:
            total_puntos[equipo_local[partido]] += 1  # Empate
            total_puntos[equipo_visita[partido]] += 1

# Función para encontrar el campeón
def calcular_campeon(total_puntos, num_equipos):
    max_puntos = total_puntos[0]
    campeon = 0
    for i in range(1, num_equipos):
        if total_puntos[i] > max_puntos:
            max_puntos = total_puntos[i]
            campeon = i
    return campeon

# Función para imprimir los puntos totales
def print_puntos_totales(equipos, total_puntos):
    print("Puntos Totales:")
    for i in range(len(equipos)):
        print(f"{equipos[i]}: {total_puntos[i]} puntos")

# Función principal
def main():
    random.seed(1234)  # Fijar semilla para la generación aleatoria

    # Lista de equipos
    equipos = ["Junior", "Millonarios", "Santafé", "Nacional", "Medellín", "Bucaramanga", "Pasto", "Alianza", "Huila", "Tolima"]
    num_equipos = len(equipos)

    # Calcular el número de partidos
    num_partidos = num_equipos * (num_equipos - 1)

    # Inicializar los vectores
    equipo_local = [0] * num_partidos
    equipo_visita = [0] * num_partidos
    goles_local = [0] * num_partidos
    goles_visita = [0] * num_partidos
    total_puntos = [0] * num_equipos

    # Generar los partidos
    generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos)

    # Calcular los puntos
    calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, total_puntos, num_partidos)

    # Encontrar al campeón
    campeon = calcular_campeon(total_puntos, num_equipos)

    # Mostrar los resultados
    print_puntos_totales(equipos, total_puntos)
    print(f"El ganador del campeonato es {equipos[campeon]} con {total_puntos[campeon]} puntos.")

if __name__ == "__main__":
    main()
