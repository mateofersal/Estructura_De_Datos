class Nodo:
    def __init__(self,valor):
        self.valor= valor 
        self.sgte = None 

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        print('hola')

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cola: 
            self.cola.sgte = nodo
            self.cola = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo

    def recorrer(self):
        actual = self.cabeza 

        while actual: 
            valor = actual.valor
            actual = actual.sgte 
            yield valor 

    def eliminar(self,valor):
        actual = self.cabeza

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


L1 = ListaEnlazada()
L2 = ListaEnlazada()
