class Pila:
    def _init_(self):
        self.elementos = []

    def apilar(self,valor):
        self.elementos.append(valor)
        return valor

    def sacar(self):
        return self.elementos.pop()

    def vacio(self):
        return len(self.elementos) == 0

    def top(self):
        return self.elementos[-1]

if _name_ == '_main_':
    pila = Pila()


    #comprobar si esta vacia
    print(pila.vacio())

    #agreagar elementos
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    pila.apilar(4)
    pila.apilar(5)

    #comprobar si esta vacia
    print(pila.vacio())

    #mostrar los elementos de la pila
    print(pila.elementos)

    #Mostrar el top
    print(pila.top())

    #sacar 2 elementos
    pila.sacar()
    pila.sacar()

    #Mostrar el top
    print(pila.top())

    #vaciar todo
    pila.sacar()
    pila.sacar()
    pila.sacar()

    #comprobar si esta vacia
    print(pila.vacio())