class Nodo:
    def __init__(self,valor):
        self.valor= valor 
        self.sgte = None 
        
class Pila:
    def __init__(self):
        self.lista=[]
        
    def apilar(self, valor):
        self.lista.append(valor)
        
    def quitar(self):
        return self.lista.pop()
       

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.text = ''
        self.lista = []

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza: 
            self.cola.sgte = nodo
            self.cola = nodo
            self.text += str(nodo.valor) + ' '
            self.lista.append(nodo.valor)
        else:
            self.cabeza = nodo
            self.cola = nodo
            self.text += str(nodo.valor) + ' '
            self.lista.append(nodo.valor)
            
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

    def next(self):
        print(self.cabeza.valor)
        self.cabeza = self.cabeza.sgte

    def __str__(self):
        return '[ ' + self.text + ']'
        
    def mayores_valor(self, valor):
        for k in self.recorrer():
            if k < valor:
                self.eliminar(k)
                
    def sacar_lista(self):
        return self.lista.pop()
        
def capicua():
    
    for k in lista.recorrer():
        if k != pila.quitar():
            return False
        else:
            return True
    
        
lista = ListaEnlazada()
lista.agregar('a')
lista.agregar('n')
lista.agregar('a')

pila=Pila()
for val in lista.recorrer():
    pila.apilar(val)
    
print(pila.lista)
print(capicua())
    

