n = 5
i = 0

while i < n:
    print("Hola mundo",i)
    i+=1

n = int(input("Ingrese un número impar: "))
while n%2 == 0:
    print("El número no fue impar")
    n = int(input("Ingrese un número impar: "))
