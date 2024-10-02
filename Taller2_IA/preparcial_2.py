import random

def isPrimo(x):
    for i in range(2,int(x**0.5)+1):
        if(x % i == 0):
            return False
    return True

def isPar(x):
    return x%2 == 0

def generarCancion(maxminutos):
    return random.randint(1,(maxminutos*60+1))
    
def generarArtista(tipo):
    noCumple = True
    if tipo == 0: #Es primo
        while(noCumple):
            id = random.randint(0,1000)+1
            if isPrimo(id):
                noCumple = False
    elif tipo == 1: #Es impar
        while(noCumple):
            id = random.randint(0,1000)+1
            if not isPar(id):
                noCumple = False
    else: #Es par
        while(noCumple):
            id = random.randint(0,1000)+1
            if isPar(id):
                noCumple = False
    return id

def conv_seg_a_minutos(segs):
    min = segs//60
    s = segs%60
    if s >= 10:
        return str(min)+":"+str(s)
    else:
        return str(min)+":0"+str(s)

def printDisco(canciones, artistas):
    tot = 0
    for i in range(len(canciones)):
        print(f"Canción {i+1}. {artistas[i]}, {conv_seg_a_minutos(canciones[i])}")
        tot += canciones[i]
    print("Duración total del disco:",conv_seg_a_minutos(tot))

def promedio(v):
    pro = 0
    for i in v:
        pro += i
    return pro//len(v)

id = int(input("Ingrese el id del disco:"))
if(isPrimo(id)):
    print(id,"es primo")
    canciones = [0]*13 #Lista de 13 canciones
    artistas = [0]*13
    for i in range(len(canciones)):
        canciones[i] = generarCancion(11)
        artistas[i] = generarArtista(0) #Generar artista primo
    
    """print(canciones)
    print(artistas)
    print(conv_seg_a_minutos(canciones[0]))"""
    
    printDisco(canciones, artistas)
    print("Promedio:",conv_seg_a_minutos(promedio(canciones)))
else:
    print(id,"no es primo")
    if isPar(id):
        print(id,"es par")
    else:
        print(id,"es impar")