#Crea la clase nodo

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
        





        


valores = ListaEnlazada()
valores.agregar(3)
valores.agregar(5)
for val in valores.recorrer():
    print(val)

print("")
valores.agregar(7)
valores.agregar(9)
for val in valores.recorrer():
    print(val)

valores.eliminar(7)
print("")
for val in valores.recorrer():
    print(val)

print(valores.buscar(3))