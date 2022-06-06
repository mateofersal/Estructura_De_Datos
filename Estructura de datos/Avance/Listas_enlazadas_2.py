class Nodo:
    def _init_(self,valor):
        self.valor = valor
        self.sgte = None

    def _str_(self):
        return str(self.valor)

class ListaEnlazada:
    def _init_(self):
        self.primero = None
        self.size = 0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.size == 0:
            self.primero = nodo
        else:
            self.elemento.append

    def _str_(self):
        actual = self.primero
        String =''
        while actual is not None:
            String +=str(actual)
            String += ' '
            actual = actual.sgte
        return String

    def eliminar(self,valor):
        actual = self.primero
        if self.size ==0:
            return False

        else:
            try: 

                while actual.sgte.valor != valor:
                    actual = actual.sgte
                nodo_a_borrar = actual.sgte
                actual.sgte = nodo_a_borrar.sgte

            except AttributeError:
                print(f'El valor {valor} no existe!')
                return False

        self.size-=1

    def buscar(self,valor):
        actual = self.primero
        while actual:
            if actual.valor == valor:
                return True
            else:
                actual= actual.sgte

        return False



#Implementar
miLista = ListaEnlazada()
miLista.agregar(5)
miLista.agregar(2)
miLista.agregar('A')
miLista.agregar('[]')
miLista.agregar('B')
print(miLista)
miLista.eliminar('A')
print(miLista)
miLista.eliminar(10)

print(miLista.buscar(6))