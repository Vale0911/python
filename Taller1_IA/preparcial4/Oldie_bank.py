edad = int(input("Ingrese su edad: "))
if edad < 20:
    base_tasa = 20.0
else:
    base_tasa = 18.0

comida_preferida = int(input("Seleccione su comida preferida: Hamburguesa = 2 / Perro = 3 / Pizza = 4 / Sushi = 5: "))

if comida_preferida == 2:
    base_tasa -= 0.2
elif comida_preferida == 3:
    base_tasa -= 0.5
elif comida_preferida == 4:
    base_tasa += 0.1
elif comida_preferida == 5:
    base_tasa += 0.3

promedio = int(input("¿Está estudiando? Sí = 1 / No = 0: "))
if promedio == 1:
    promedio_si = float(input("Ingrese su promedio: "))
    if promedio_si < 3.5:
        base_tasa -= 0.5
    elif 3.5 <= promedio_si <= 4.2:
        base_tasa -= 0.8
    elif promedio_si > 4.2:
        base_tasa -= 1.5


if base_tasa < 0:
    base_tasa = 0

tasa_final = base_tasa
print("Tasa final de interés:", tasa_final)

labora = int(input("¿Trabaja? Sí = 1 / No = 0: "))
if labora == 1 and tasa_final < 17.0:
    tasa_final -= 1.0

if tasa_final < 0:
    tasa_final = 0

print("Su tasa final de interés:", tasa_final)





    
