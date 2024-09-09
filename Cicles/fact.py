fact = 1
i=1
n = int(input("Ingrese un número n: "))
while (i<=n):
    fact *= i
    i+=1
    print ("El factorial de ",(i==1),"es: ",fact)
print ("El factorial de n es: ",fact)