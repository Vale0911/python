opcion = 0

areaHabitaciones = 0
areaBanhos = 0


areaPatio = 0
opcion = int(input("¿La casa tiene patio? No=0, Sí=1 "))
if opcion == 1:
    largo = int(input("Ingrese el largo del patio: "))
    if largo < 2:
        largo = 2
    elif largo > 8:
        largo = 8
    
    #largo = max(largo, 2);
    #largo = min(largo, 8);
    
    ancho = int(input("Ingrese el ancho del patio: "))
    if ancho < 2:
        ancho = 2
    elif ancho > 8:
        ancho = 8
    
    areaPatio = largo*ancho

print("Area patio",areaPatio)



areaSocial = 20
opcion = int(input("¿Qué tipo de area social desea? Regular=0, Premium=1 "))
if opcion == 1:
    areaSocial = 40

print("Area social",areaSocial)

areaGaraje = 10
opcion = int(input("¿Qué tipo de garaje social desea? Estándar=0, Doble=1 "))
if opcion == 1:
    areaGaraje = 20
    
print("Area garaje",areaGaraje)


areaTotal = (areaHabitaciones + areaBanhos + areaPatio + areaSocial)*1.25
print("El area total de la casa, incluido el garaje, es ",(areaTotal+areaGaraje))

if areaTotal < 100:
    valorTotal = areaTotal * 8000000
else:
    valorTotal = areaTotal * 9000000

valorTotal = valorTotal + areaGaraje*5000000

if valorTotal > 1000000000:
    valorTotal = valorTotal*(0.95)


print("El valor total de la casa es ",valorTotal)