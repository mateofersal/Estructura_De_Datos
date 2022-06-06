#Crea la clase nodo

class Nodo:
    def __init__(self,valor):
        self.valor= valor 
        self.sgte = None 

class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None: 
            self.cabeza = nodo
            self.cola = nodo
            self.size += 1
        else:
            self.cola.sgte = nodo
            self.cola = nodo
            self.cola.sgte = self.cabeza
            self.size +=1
            
    def recorrer(self):
        actual = self.cabeza 
        for k in range(self.size):
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
            self.size-=1
        except AttributeError:
            print(f'El valor {valor} no existe!')
            return False


    def buscar(self,valor):
        for val in self.recorrer():
            if val == valor:
                return True

            else:
                return False
        


lista = ListaCircular()
lista.agregar(6)
lista.agregar(4)
lista.agregar(5)
lista.agregar(7)
lista.recorrer()
print('eliminando el 5')
lista.eliminar(5)
lista.recorrer()


        

