class Nodo:
    def __init__(self,valor):
        self.valor= valor 
        self.sgte = None 
       

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.text = ''

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza: 
            self.cabeza.sgte = nodo
            self.cabeza = nodo
            self.text += str(nodo.valor) + ' '
        else:
            self.cabeza = nodo
            self.cola = nodo
            self.text += str(nodo.valor) + ' '
            

    def recorrer(self):
        actual = self.cola 

        while actual: 
            valor = actual.valor
            actual = actual.sgte 
            print(valor)

    def eliminar(self,valor):
        actual = self.cola
        try: 
            while actual.sgte.valor != valor:
                actual = actual.sgte
            nodo_a_borrar = actual.sgte
            actual.sgte = nodo_a_borrar.sgte
        except AttributeError:
            print(f'El valor {valor} no existe!')
            return False


    def buscar(self,valor):
        for val in self.recorrer():
            if val == valor:
                return True
            else:
                return False

    def next(self):
        print(self.cola.valor)
        self.cola = self.cola.sgte

    def __str__(self):
        return '[ ' + self.text + ']'


lista = ListaEnlazada()
lista.agregar(3)
lista.agregar(7)
lista.agregar(4)
lista.agregar(2)
lista.recorrer()
print('elemento a elemento')
lista.next()
lista.next()
lista.next()
lista.next()
print(lista)

#R./ Si es necesario agregar un a
