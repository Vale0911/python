# Escribe un programa que tome una cadena de texto del usuario y cuente cuántas vocales hay en la cadena
usuario = input("Deje su mensaje:")

vocales = 'aeiou'
cont = 0
for letra in usuario:
    if letra.lower() in vocales:
        cont += 1
print(f'La cantidad de vocales en su mensaje es {cont}')  # No se puede
