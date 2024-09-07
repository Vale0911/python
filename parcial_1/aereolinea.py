print("Bienvenidos a Aerolíneas Nueva Scadta")
distancia_v = int(input("Ingrese la distancia de su vuelo en km: "))

valor_pasaje = 10000 * distancia_v
puntos_acumulados = distancia_v

valor_pasaje = valor_pasaje * 1.25

estatus = int(input("Ingrese su estatus: 0: no tiene, 1: Bronce, 2: Plata, 3: Oro: "))
if estatus == 1:  # Bronce
    valor_pasaje = 9000 * distancia_v * 1.25
    puntos_acumulados = distancia_v #corrección puntos que acumula 
elif estatus == 2:  # Plata
    valor_pasaje = 7500 * distancia_v * 1.25
    puntos_acumulados = distancia_v * 2
elif estatus == 3:  # Oro
    valor_pasaje = 6000 * distancia_v * 1.25
    puntos_acumulados = distancia_v * 4

# Agregar puntos disponibles si tiene estatus
if estatus != 0:
    puntos = int(input("Ingrese cuántos puntos tiene: "))
    desea_pagar_con_puntos = int(input("Desea pagar con puntos: 0: No, 1: Sí: "))
    
    if desea_pagar_con_puntos == 1:
        valor_en_pesos_de_puntos = puntos * 2000
        if valor_en_pesos_de_puntos >= valor_pasaje:
            puntos_restantes = (valor_en_pesos_de_puntos - valor_pasaje) // 2000
            valor_pasaje = 0
            puntos_acumulados = puntos_restantes
            print("Ha pagado con sus puntos. Le quedan", puntos_acumulados, "puntos.")
        else:
            saldo_pendiente = valor_pasaje - valor_en_pesos_de_puntos
            puntos_acumulados = 0
            print("El valor final de su tiquete es:", saldo_pendiente, "y no le quedan puntos disponibles.")
    else:
        puntos_acumulados += puntos
        print("El valor final de su tiquete es:", valor_pasaje, "y tiene", puntos_acumulados, "puntos disponibles.")
else:
    print("El valor de su tiquete es:", valor_pasaje)

