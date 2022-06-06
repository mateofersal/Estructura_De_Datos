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
            self.cola.sgte = nodo
            self.cola = nodo
            self.text += str(nodo.valor) + ' '
        else:
            self.cabeza = nodo
            self.cola = nodo
            self.text += str(nodo.valor) + ' '
            

    def recorrer(self):
        actual = self.cabeza
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

    def __str__(self):
        return '[ ' + self.text + ']'

    def invertir(self):
        act = self.cabeza
        ant = None
        while act:
            siguiente  = act.sgte
            act.sgte = ant
            ant = act
            act = siguiente
        self.cola, self.cabeza = self.cabeza, self.cola
            
            



lista = ListaEnlazada()
lista.agregar(3)
lista.agregar(7)
lista.agregar(4)
lista.agregar(2)
lista.recorrer()
print('elemento a elemento')
lista.recorrer()
print('lista invertida')
lista.invertir()
lista.recorrer()




#R./ Si es necesario agregar un a
