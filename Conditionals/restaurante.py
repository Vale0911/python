print("Arma tu hamburguesa a tu elección:")

total= 15000
cantidad = int(input("¿Cuántos hamburguesas deseas? "))
total=(cantidad*total)

carnes= int(input("¿desea carnes? (1) Si / (2) No "))
if carnes==1:
    carnes= int(input("¿Cuántas carnes deseas? "))
    total=total+5000

quesos= int(input("¿desea quesos? (1) Si / (2) No "))
if quesos==1:
    quesos= int(input("¿Cuántos quesos deseas? "))
    total=total+10000

tocinetas= int(input("¿desea tocinetas? (1) Si / (2) No"))
if tocinetas==1:
    tocinetas= int(input("¿Cuántas tocinetas deseas? "))
    total=total+15000

pepinillos= int(input("¿desea pepinillos? (1) Si / (2) No "))
if pepinillos==1:
    pepinillos= int(input("¿Cuántos pepinillos deseas? "))
    total=total+10000

verduras= int(input("¿desea verduras? (1) Si / (2) No"))
if verduras==1:
    verduras= int(input("¿Cuántas verduras deseas? "))
    total=total+10000

print("El total de su pedido es:", total)