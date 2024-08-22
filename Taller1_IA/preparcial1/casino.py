import random

semilla = 10000
random.seed(semilla)
min_val = 1
max_val = 6

tiro_inicial = random.randint(min_val, max_val)
print("Tiro inicial:",tiro_inicial)

if tiro_inicial == 7 or tiro_inicial == 11:
        print("Ganaste!")
elif tiro_inicial in [2, 3, 12]:
        print("Perdiste!")
else:
        puntos_sumados = tiro_inicial
        tiro_secundario = random.randint(min_val, max_val)
        print("Tiro siguiente:",tiro_secundario)

        if tiro_secundario == puntos_sumados:
            print("Ganaste!")
        elif tiro_secundario == 7:
            print("Perdiste!")
        else:
            print("No ganaste ni perdiste, sigue jugando!")

