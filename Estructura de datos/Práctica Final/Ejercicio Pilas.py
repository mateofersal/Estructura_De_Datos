class Pila:
    def __init__(self):
        self.lista= []

    def apilar(self, palabra):
        for k in palabra:
            self.lista.append(k)
    
    def desapilar(self):
        return self.lista.pop()

    def mostrar(self):
        for k in self.lista:
            print(k, end='\n')

    def capicua(self):
        for k in self.lista:
            if k != self.desapilar():
                return False
        return True



a = input('Verifique si es capicua: ')
pila = Pila()
pila.apilar(a)
pila.mostrar()
print(pila.capicua())
