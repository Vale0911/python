contrasenha = 1234
intentos = 0


intento = int(input("ingrese su contrasenha: "))
while intento != contrasenha and intentos <2:
    print("Clave inconrrecta. Tiene ",2-intentos,"intentos más")
    intentos +=1
    intento = int(input("Ingrese su contraseña: "))

if intento != contrasenha:
    print("cuanta bloqueada!!")
else:
    print ("Bienvenido a su cuenta!!")

