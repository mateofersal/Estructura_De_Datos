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

    def quitar_elemento(self, n):
        for k in self.elementos:
            if k == n:
                self.elementos.remove(k)

    def ingresar_n(self, valor, n):
        for k in range (len(self.elementos)):
            if k == n-1:
                self.elementos.insert(k, valor)


pila=Pila()
pila.apilar(2)
pila.apilar(3)
pila.apilar(5)
pila.apilar(10)
print('pila en orden inicial')
pila.mostrar()
pila.ingresar_n(1, 2)
print('\napilando 1 en el lugar del segundo')
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

    def quitar_elemento(self, n):
        for k in self.elementos:
            if k == n:
                self.elementos.remove(k)

    def ingresar_n(self, valor, n):
        for k in range (len(self.elementos)):
            if k == n-1:
                self.elementos.insert(k, valor)

cola = Cola()
cola.encolar(5)
cola.encolar(8)
cola.encolar(7)
print('\n\ncola en orden inicial')
cola.mostrar()
cola.ingresar_n(3, 3)
print('\nencolando el 3 en la tercera posicion')
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
            yield valor 

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
        
    def meter_lugar(self, valor, n):
        actual = self.cola
        nodo = Nodo(valor)
        n = n-1
        cont=0
        while n!= cont:
            actual = actual.sgte
            cont+=1

        nodo.sgte = actual.sgte
        actual.sgte = nodo
        
                
        
       

print('\n\nnodos')
valores = ListaEnlazada()
valores.agregar(3)
valores.agregar(5)
valores.agregar(7)
valores.agregar(9)
for val in valores.recorrer():
    print(val)

print('metiendo 2 en la tercera posicion')
valores.meter_lugar(2, 3)
print("")
for val in valores.recorrer():
    print(val)

