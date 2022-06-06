class Pila:
    def __init__(self):
        self.elementos=[]

    def apilar(self, valor):
        self.elementos.append(valor)

    def quitar(self):
        self.elementos.pop()

    def top(self):
        print(self.elementos[-1])

    def vacia(self):
        return len(self.elementos)==0

    def contar(self):
        cont = 0
        for k in self.elementos:
            cont+=1
        print(cont)

    def invertir(self):
        self.elementos.reverse()

    def mostrar(self):
        for k in self.elementos:
            print(k, end='')

pila=Pila()
pila.apilar(2)
pila.apilar(3)
print('pila en orden inicial')
pila.mostrar()
pila.invertir()
print('\npila en orden invertido')
pila.mostrar()

class Cola:
    def __init__(self):
        self.elementos=[]

    def encolar(self, valor):
        self.elementos.append(valor)

    def quitar(self):
        self.elementos.pop()

    def ultimo(self):
        print(self.elementos[-1])

    def primero(self):
        print(self.elementos[0])

    def vacia(self):
        return len(self.elementos)==0

    def contar(self):
        cont = 0
        for k in self.elementos:
            cont+=1
        print(cont)

    def invertir(self):
        self.elementos.reverse()

    def mostrar(self):
        for k in self.elementos:
            print(k, end='')

cola = Cola()
cola.encolar(5)
cola.encolar(8)
cola.encolar(7)
print('\n\ncola en orden inicial')
cola.mostrar()
cola.invertir()
print('\ncola en orden invertido')
cola.mostrar()


class Nodo:
    def __init__(self,valor):
        self.valor= valor 
        self.sgte = None 

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza: 
            self.cabeza.sgte = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo

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

    def contar(self):
        actual = self.cola
        cont=0
        while(actual):
            cont+=1
            actual = actual.sgte
        print(cont)

    def invertir(self):
        act = self.cola
        ant = None
        while act:
            siguiente  = act.sgte
            act.sgte = ant
            ant = act
            act = siguiente
        self.cola, self.cabeza = self.cabeza, self.cola


lista = ListaEnlazada()
lista.agregar(6)
lista.agregar(9)
lista.agregar(7)
print('\n\nnodos con referencia al siguiente')
lista.recorrer()
lista.invertir()
print('\nnodos con referencia al anterior (lista invertida)')
lista.recorrer()

    