class Nodo:
    def __init__(self, valor):
        self.valor = valor

class ListaEnlazada:
    def __init__(self):
        self.elementos=[]

    def mete(self, valor):
        nodo = Nodo(valor)
        if len(self.elementos)!=0:
            self.elementos.append(nodo.valor)
        else:
            self.elementos.append(nodo.valor)

        self.elementos.sort()


    def saca(self, valor):
        if len(self.elementos)==0:
            print('la lista esta vacia')
        else:
            for k in range(len(self.elementos)):
                if self.elementos[k] == valor:
                    self.elementos.pop(k)    
                    print('esta el valor')
                self.elementos.sort()

    def lista(self):
        for k in self.elementos:
            if k is not None:
                print(k)

lista1 = ListaEnlazada()

lista1.mete(5)
lista1.mete(7)
lista1.mete(10)
lista1.mete(4)

print(lista1.lista())

lista1.saca(10)

print(lista1.lista())