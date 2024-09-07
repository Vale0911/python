import math 

x = float(input("Ingrese el valor de x:"))
y = float(input("Ingrese el valor de y:"))


p_uno = math.sqrt((math.pow(x,y)) * ((math.sqrt((math.pow(y,x))+3))/8))

p_dos = (32 * y - 5 ) / ( math.pow( x * y, 2))

p_tres = (12 * y - math.pow(x , 2+y) * 2 ) / p_dos

c = math.pow (p_tres,3)

z = math.pow(p_uno , 3)/math.pow(c , 3)

print(z)
