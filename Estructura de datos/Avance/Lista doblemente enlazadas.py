class Nodo:
    def __init__(self,valor):
        self.valor = valor 
        self.sgte = None 
        self.ante = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None: 
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.ante = self.cola   	#faltaba agregar el link al anterior nodo
            nodo.sgte = self.cabeza
            self.cola = nodo
            self.cabeza.ante = self.cola
            
        self.size +=1

    def agregar_inicio(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.sgte = self.cabeza  #este siempre es cabeza porque nunca se modifica es asi por que si
            self.cabeza.ante = nodo
            self.cabeza = nodo
        self.size+=1

    def agregar_mitad(self, valor):
        actual = self.cabeza
        nodo = Nodo(valor)
        mitad = self.size//2
        cont=0
        while(cont<mitad):
            actual = actual.sgte
            cont+=1
        nodo.ante = actual.ante
        nodo.sgte = actual
        actual.ante.sgte = nodo
        actual.ante = nodo
        self.size+=1

    def recorrer(self):
        actual = self.cabeza 
        while actual: 
            valor = actual.valor
            actual = actual.sgte 
            yield valor 

    def recorrer_de_atras(self):
        actual = self.cola
        while actual:
            valor = actual.valor
            actual = actual.ante
            yield valor

lista = ListaEnlazadaDoble()
lista.agregar(7)
lista.agregar(4)
lista.agregar(8)
lista.agregar_inicio(5)
lista.agregar_mitad(2)
lista.agregar_mitad(3)

print('lista en orden: ')
for k in lista.recorrer():
   print(k)

print('lista recorrida desde atras: ')
for k in lista.recorrer_de_atras():
    print(k)


print()