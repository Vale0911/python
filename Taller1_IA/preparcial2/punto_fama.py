import sys
secreto = int(input("Juagdor A, ingrese el número secreto de dos dígitos:"))

if secreto < 10 or secreto >99:
    print("Número inválido. Gracias por participar")
else :
    digito_secreto1 = secreto //10
    digito_secreto2 = secreto % 10

    intento = int(input("Jugador B, ingrese su primer intento:"))
    digito_intento1= intento //10
    digito_intento2 = intento % 10

    if intento == secreto:
        print("Usted ha encontrado en número secreto!")
        sys.exit ()
    elif digito_intento1 == digito_intento2 and digito_intento2 == digito_secreto1:
        print('Usted tiene 2 puntos')
    elif digito_intento1 == digito_secreto1 or digito_intento2 == digito_secreto2:
        print("Usted tiene 1 fama")
    elif digito_intento1 == digito_secreto2 or digito_intento2== digito_secreto1:
        print("Usted tiene 1 punto")
    
    intento =int(input("Juagdor B, ingrese su segundo intento"))

    digito_intento1 = intento // 10
    digito_intento2 = intento % 10

    if intento == secreto:
        print("Usted ha encontrado el número secreto!")
        sys.exit ()
    elif digito_intento1 == digito_intento2 and digito_intento2 == digito_secreto1:
        print("Usted tiene 2 puntos")
    elif digito_intento1 == digito_secreto1 or digito_intento2 == digito_secreto2:
        print("Usted tiene 1 fama")
    elif digito_intento1 == digito_secreto2 or digito_intento2== digito_secreto1:
        print("Usted tiene 1 punto")
    
    intento =int(input("Juagdor B, ingrese su tercer intento"))

    digito_intento1 = intento // 10
    digito_intento2 = intento % 10

    if intento == secreto:
        print("Usted ha encontrado el número secreto!")
        sys.exit ()
    elif digito_intento1 == digito_intento2 and digito_intento2 == digito_secreto1:
        print("Usted tiene 2 puntos")
    elif digito_intento1 == digito_secreto1 or digito_intento2 == digito_secreto2:
        print("Usted tiene 1 fama")
    elif digito_intento1 == digito_secreto2 or digito_intento2== digito_secreto1:
        print("Usted tiene 1 punto")
    
    intento =int(input("Juagdor B, ingrese su cuarto intento"))

    digito_intento1 = intento // 10
    digito_intento2 = intento % 10

    if intento == secreto:
        print("Usted ha encontrado el número secreto!")
        sys.exit ()
    elif digito_intento1 == digito_intento2 and digito_intento2 == digito_secreto1:
        print("Usted tiene 2 puntos")
    elif digito_intento1 == digito_secreto1 or digito_intento2 == digito_secreto2:
        print("Usted tiene 1 fama")
    elif digito_intento1 == digito_secreto2 or digito_intento2== digito_secreto1:
        print("Usted tiene 1 punto")
    
    intento =int(input("Juagdor B, ingrese su quinto intento"))

    digito_intento1 = intento // 10
    digito_intento2 = intento % 10

    if intento == secreto:
        print("Usted ha encontrado el número secreto!")
    else:
        print("Juagdor B, ha perdido. El número era:",secreto)
    
    
