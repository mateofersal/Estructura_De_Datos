class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    
    def __str__(self):
        return self.nombre+'-'+str(self.edad)+' años'

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.sgte = None 


class Pila:
    def __init__(self):
        self.elementos=[]
        self.ultimo = None

    def mete(self, nodo):
        if self.ultimo is None:
            self.elementos.append(nodo.nombre)
            self.ultimo = nodo
        else:
            self.elementos.append(nodo.nombre)
            self.ultimo = nodo

    def saca(self):
        if len(self.elementos)==0:
            print('la lista esta vacia')
        else:
            elemento = self.ultimo
            self.elementos.pop()
            self.ultimo = self.elementos[len(self.elementos)-1]
            return elemento

    

    def lista(self):
        for k in self.elementos:
            if k is not None:
                print(k)

primero = None
alumno1 = Alumno('Alex', 30, 8.9)
nodo = Nodo(alumno1)
nodo.sgte = primero
primero = nodo

alumno2 = Alumno('Pepe',27, 3.7)
nodo = Nodo(alumno2)
nodo.sgte = primero
primero = nodo

alumno3 = Alumno('Mateo', 20, 3.7)

n = primero
while n != None:
    print(n.datos)
    n = n.sgte

pila = Pila()
print('apilacion de nombres')
pila.mete(alumno1)
pila.mete(alumno2)
print(pila.elementos)

print('removiendo el ultimo')
print('quitando a: ', pila.saca())
print(len(pila.elementos))
print('pila actual')
print(pila.lista())

