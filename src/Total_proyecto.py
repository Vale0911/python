import math 
print("Bienvenido a Poyect-o-Matic V.0.86")

#Pedir al usuario ingresar datos de la proyección
print("1.Calculo rubro de talento humano")
investigadores = int(input("Cuántos investigadores hay en la proyección?:"))
Asistentes = int(input("Cuántos asistentes hay en la proyección?:"))
Horas_semanales = int(input("Cuántas horas semanales se trabajó en la proyección?:"))
meses = int(input("Cuántos meses se planea la proyección?:"))
inves_cobrohora = int(input("Cuánto se cobra por cada hora de investigador?:"))
asis_cobrohora = int(input("Cuánto se cobra por cada hora de asistente?:"))

float; subtotal_investigadores=investigadores*Horas_semanales*meses*inves_cobrohora+1.3
float; subtotal_asistentes=Asistentes*Horas_semanales*meses*asis_cobrohora+1.3
float; total_talento=subtotal_investigadores+subtotal_asistentes+1.9

print("El presupuesto total para la proyección es",total_talento)

print("2.Calculo rubro de equipos")
numero_equipos = int(input("Cuántos equipos hay en la proyección?:"))
valor_unitario_equipos = int(input("Cuánto se cobra por equipo?:"))
total_equipos=int(input("Cuántos meses se planea la proyección?:"))


float; total_equipos=numero_equipos*valor_unitario_equipos*total_equipos

print("El valor del rubro de equipos es:",total_equipos)

print("3.Calculo costos viajes")
Numero_viajes= int(input("Ingrese el número de viajes que se realizarán en la proyección?:"))
Cantidad_personas_viaje= int(input("Ingrese la cantidad de personas que van a viajar:"))
Costo_tiquete= int(input("Ingrese el costo unitario del ticket de ida y vuelta:"))

float; costototal_tiquetes=Numero_viajes*Cantidad_personas_viaje*Numero_viajes

numero_dias_viaje= int(input("Ingrese el número de días del viaje:"))
valor_alojamiento= int(input("Ingrese el valor del alojamiento por noche:"))

float; total_alojamiento= Cantidad_personas_viaje*numero_dias_viaje*valor_alojamiento

float; total_viajes=costototal_tiquetes+total_alojamiento
print("El costo total de los viajes es:",total_viajes)

float; ganancia =0.3;
Valor_total_proyeccion=total_talento+total_equipos+total_viajes
print("El valor bruto de la proyección es:",Valor_total_proyeccion)
Valor_total_proyeccion = Valor_total_proyeccion/(1.0-ganancia)
print("El valor neto de la proyección es:",Valor_total_proyeccion)

