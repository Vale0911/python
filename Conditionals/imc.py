import math
print ("Indice de masa corporal en adultos")


peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))
IMC = peso / (estatura ** 2)
total=IMC
# Calculando el índice de masa corporal (IMC)
print("Su IMC es: ", total)
if IMC < 18.5:
    print("Bajo peso")
    print("Su recomendación es: Comer más y beber menos alimentos")
elif 18.5 <= IMC < 25:
    print("Peso normal")
    print("Su recomendación es: Comer lo que se comija y seguir ejercitándose")
elif 25 <= IMC < 30:
    print("Sobrepeso")
    print("Su recomendación es: Sea consciente de que tiene sobrepeso y comience a comer menos")
elif 30 <= IMC < 35:
    print("Obesidad grado I")
    print("Su recomendación es: Sea consciente de que tiene obesidad grado I y comience a comer menos")
elif 35 <= IMC < 40:
    print("Obesidad grado II")
    print("Su recomendación es: Sea consciente de que tiene obesidad grado II y comience a comer menos")
else:
    print("Obesidad grado III")
    print("Su recomendación es: Sea consciente de que tiene obesidad grado III y comience a comer menos")

# Calculando el índice de masa corporal (IMC) en kg/m²
