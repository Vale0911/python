import math

n = int(input("Escriba el máximo número a evaluar: "))

if(n>=2):
    print("2 es primo!")

#for(int j = 3; j<=n; j+=2):
for j in range(3,n+1,2):
    i = 2
    while(i < math.sqrt(j) and j%i != 0):
        i+=1
    
    if(i>math.sqrt(j)):
        print(j," es primo!")
    else:
        print(j," no es primo!")
