class Pila:
    def __init__(self):
        self.elementos=[]

    def apilar(self, valor):
        self.elementos.append(valor)
        return valor

    def desapilar(self):
        self.elementos.pop()
    

def calcular(pila, indice):
    if pila.elementos[indice]!= None:
        return 1 + calcular(pila, indice+1)
    else:
        return  1
        
pila = Pila()
pila.apilar(3)
pila.apilar(4)
pila.apilar(7)
pila.apilar(8)
pila.apilar(None)
print('la pila contiene ', calcular(pila, 0), 'elementos')

