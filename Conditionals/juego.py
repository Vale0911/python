print("Piensa en un número entre 0 y 10 y el juego intentará adivinarlo.")

# Primera adivinanza
respuesta = input("¿Es tu número 5? (s/n): ").lower()
if respuesta == 's':
    print("¡He adivinado tu número! Es 5.")
else:
    mayor = input("¿Tu número es mayor que 5? (s/n): ").lower()
    if mayor == 's':
        # Segunda adivinanza para números mayores que 5
        respuesta = input("¿Es tu número 8? (s/n): ").lower()
        if respuesta == 's':
            print("¡He adivinado tu número! Es 8.")
        else:
            mayor = input("¿Tu número es mayor que 8? (s/n): ").lower()
            if mayor == 's':
                respuesta = input("¿Es tu número 9? (s/n): ").lower()
                if respuesta == 's':
                    print("¡He adivinado tu número! Es 9.")
                else:
                    print("¡He adivinado tu número! Es 10.")
            else:
                respuesta = input("¿Es tu número 6? (s/n): ").lower()
                if respuesta == 's':
                    print("¡He adivinado tu número! Es 6.")
                else:
                    print("¡He adivinado tu número! Es 7.")
    else:
        # Segunda adivinanza para números menores o iguales a 5
        respuesta = input("¿Es tu número 2? (s/n): ").lower()
        if respuesta == 's':
            print("¡He adivinado tu número! Es 2.")
        else:
            mayor = input("¿Tu número es mayor que 2? (s/n): ").lower()
            if mayor == 's':
                respuesta = input("¿Es tu número 4? (s/n): ").lower()
                if respuesta == 's':
                    print("¡He adivinado tu número! Es 4.")
                else:
                    print("¡He adivinado tu número! Es 3.")
            else:
                respuesta = input("¿Es tu número 0? (s/n): ").lower()
                if respuesta == 's':
                    print("¡He adivinado tu número! Es 0.")
                else:
                    print("¡He adivinado tu número! Es 1.")
