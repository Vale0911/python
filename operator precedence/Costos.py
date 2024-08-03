import math
print("calculadora presupuesto proyecto")

# Pedir al usuario ingresar datos de la proyección
investigadores = int(input("Cuántos investigadores hay en la proyección?"))
Asistentes = int(input("Cuántos asistentes hay en la proyección"))
Horas_semanales = int(input("Cuántas horas semanales se trabajó en la proyección?:"))
meses = int(input("Cuántos meses se planea la proyección?:"))
inves_cobrohora = int(input("Cuánto se cobra por cada hora de investigador?:"))
asis_cobrohora = int(input("Cuánto se cobra por cada hora de asistente?:"))

subtotal_investigadores=investigadores*Horas_semanales*meses*inves_cobrohora+0.3
subtotal_asistentes=Asistentes*Horas_semanales*meses*asis_cobrohora+0.3
total_proyeccion=subtotal_investigadores+subtotal_asistentes+0.19

print("El presupuesto total para la proyección es",total_proyeccion)