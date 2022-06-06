import random

class Avion:
    def __init__(self):
        self.prioridad = random.randrange(2)

class TorreDeControl:
    def __init__(self):
        self.despegue = []
        self.aterrizaje = [] 
        self.muestreo = []

    def reconocimiento(self, avion):
        if avion.prioridad == 1:
            self.aterrizaje.append(avion)
        else:
            self.despegue.append(avion)
    
    def accion(self):
        while len(self.aterrizaje)!=0:
            print('\nAccion: aterrizaje')
            print(self)
            self.aterrizaje.pop(0)
            self.muestreo
        while len(self.despegue)!=0:
            print('\nAccion: despegue')
            print(self)
            self.despegue.pop(0)

        print('')

    def __str__(self):
        return 'Estado \nAterrizaje: '+ str(len(self.aterrizaje)) + ' - Despegue: '+str(len(self.despegue))

    

lugar = TorreDeControl()
lugar.reconocimiento(Avion())
lugar.reconocimiento(Avion())
lugar.reconocimiento(Avion())
lugar.reconocimiento(Avion())
lugar.reconocimiento(Avion())

print('\nEstado inicial de los aviones ')
print(lugar)

while len(lugar.aterrizaje) > 0 or len(lugar.despegue) > 0:
    lugar.accion()

