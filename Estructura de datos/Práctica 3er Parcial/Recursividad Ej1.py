# crear una funcion recursiva que determine el tiempo en que una rata obtiene su libertad a partir de 3 caminos elegidos al azar
# camino 1 - 3 minutos y vuelve a jaula
# camino 2 - 5 minutos y vuelve a jaula
# camino 3 - 7 minutos y sale de la jaula

import random

def tiempo_rata(camino):
    camino_sgte = random.randint(1,3)
    if camino==1:
        print('camino 1 - 3 minutos')
        return 3 + tiempo_rata(camino_sgte)
    elif camino ==2:
        print('camino 2 - 5 minutos')
        return 5 + tiempo_rata(camino_sgte)
    elif camino==3:
        print('camino 3 - 7 minutos')
        return 7

camino = random.randint(1,3)
print('el tiempo que la rata emplea en obtener su libertad es: ', tiempo_rata(camino))