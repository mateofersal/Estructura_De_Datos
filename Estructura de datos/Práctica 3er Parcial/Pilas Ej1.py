class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return self.palo + ' ' + str(self.valor)

class PilaDeCartas:
    def __init__(self):
        self.cartas=[]
        self.valor_ante = None
        self.palo_ante = None
        self.muestra = ''

    def apilar(self, palo, valor):
        carta = Carta(palo, valor)
        if self.valor_ante is None:
            self.valor_ante = valor
            self.palo_ante = palo
            self.muestra += palo + ' '+ str(valor) + '\n'
            self.cartas.append(carta)
            
            print(carta)
        else:
            if palo != self.palo_ante and valor < self.valor_ante:
                self.cartas.append(carta)
                self.palo_ante = palo
                self.valor_ante = valor
                self.muestra += palo + ' '+ str(valor) + '\n'
                print(carta)
            else:
                print('palo es igual o valor no es inferior')

    def __str__(self):
        return self.muestra

print('aplilando las cartas')
pila = PilaDeCartas()
pila.apilar('espada', 10)
pila.apilar('espada', 7)
pila.apilar('picas', 3)
pila.apilar('trebol', 4)
print('\ntotal de cartas apiladas hasta ahora: ')
print(pila)