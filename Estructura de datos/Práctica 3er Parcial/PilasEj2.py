#creacion de lista e insercion de elemento viejo con nuevo

class Pila:
    def __init__(self):
        self.elementos=[]
    
    def apilar(self, valor):
        self.elementos.append(valor)

    def insercion(self, viejo, nuevo):
        aux=0
        while(self.elementos[aux]!=viejo):
            aux+=1
            elemento=self.elementos[aux]
            
        print('el agarrado es: ',elemento)
        if(viejo==elemento):
            self.elementos[aux]=nuevo
        else:
            print('El elemento no esta en la pila')

pila=Pila()
pila.apilar(3)
pila.apilar(7)
pila.apilar(4)
pila.apilar(2)

print('pila actual',pila.elementos)

print('insercion de 10 en lugar de 4')
pila.insercion(4,10)

print('nueva pila', pila.elementos)

