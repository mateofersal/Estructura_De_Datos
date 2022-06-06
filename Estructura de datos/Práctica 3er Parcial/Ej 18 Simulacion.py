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


class Cola:
    def __init__(self):
        self.elementos=[]
        self.ultimo = None
        self.primero = None

    def mete(self, nodo):
        if self.primero is None:
            self.elementos.append(nodo.nombre)
            self.ultimo = nodo
            self.primero = nodo
        else:
            self.elementos.append(nodo.nombre)
            self.ultimo = nodo

    def saca(self):
        if len(self.elementos)==0:
            print('la lista esta vacia')
        else:
            elemento = self.primero
            self.elementos.pop(0)
            self.primero = self.elementos[0]
            return elemento

    def lista(self):
        for k in self.elementos:
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
nodo = Nodo(alumno3)
nodo.sgte = primero
primero = nodo

cola = Cola()
cola.mete(alumno1)
cola.mete(alumno2)
cola.mete(alumno3)
print(cola.lista())

print('quitando el primero', cola.primero)
cola.saca()
print(cola.lista())


