class Pila:
    def __init__(self):
        self.elementos=[]

    def agregar(self,valor):
        self.elementos.append(valor)

    def vacia(self):
        return len(self.elementos)==0

    def quitar(self):
        self.elementos.pop()

    def top(self):
        

    def contar(self):
        cont=0
        for k in self.elementos:
            cont+=1
        print(cont)
    

pila = Pila