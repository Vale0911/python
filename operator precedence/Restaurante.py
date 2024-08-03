print("Elige tu hamburguesa:")

total = 15000
carnes = int(input("Cuántas carnes quiere?"))
total = total + carnes*5000
quesos = int(input("Cuántos quesos quiere?"))
total = total + quesos*2500
cantidad = int(input("Cuántas hamburquesas quiere?"))
total = (cantidad*total)*1.19
Tocinetas= int(input("Cuántas tocinetas quiere?"))
total = total + Tocinetas*3000
pepinillos = int(input("Cuántos pepinillos quiere?"))
total=total + pepinillos*1000
verduras = int(input("Cuántas verduras quiere?"))
total=total + verduras*700
print("El total es",total)