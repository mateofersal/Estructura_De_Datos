class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.sgte = None

    def __str__(self):
        return str(self.valor)

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0
        self.eliminados = 0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.size == 0:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.sgte is not None:
                actual = actual.sgte
            actual.sgte = nodo
        self.size = self.size + 1

    def __str__(self):
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
                if actual.valor == valor:
                    self.primero = actual.sgte
                else:
                    while actual.sgte.valor != valor:
                        actual = actual.sgte
                    nodo_a_borrar = actual.sgte
                    actual.sgte = nodo_a_borrar.sgte
                    

            except AttributeError:
                print(f'El valor {valor} no existe!')
                return False

        self.size-=1
        self.eliminados+=1

    def buscar(self,valor):
        actual = self.primero
        while actual:
            if actual.valor == valor:
                return True
            else:
                actual= actual.sgte

        return False

    def invertir(self):
        act = self.cola
        anterior = None
        while act:
            siguiente = act.sgte
            act.sgte = anterior
            anterior = act
            act = siguiente
        self.cola, self.cabeza = self.cabeza, self.cola

    def convertir_a_vector(self):
        actual = self.primero
        v = []
        while actual:
            v.append(actual.valor)
            actual= actual.sgte
        print(v)

#def eliminar_en_2(lista1,lista2):
    


        


#lista
lista1 = ListaEnlazada()
lista1.agregar('e')
lista1.agregar('m')
lista1.agregar('x')
lista1.agregar('i')

lista2 = ListaEnlazada()
lista2.agregar('t')
lista2.agregar('e')
lista2.agregar('e')
lista2.agregar('r')

print('Lista 1')
print(lista1)

print('---------')

print('Lista 2')
print(lista2)

print('eliminando la x')
lista1.eliminar('x')
print(lista1)