class Nodo:
    def __init__(self,valor):
        self.valor = valor 
        self.sgte = None 
        self.ante = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
        self.cant_elim = 0 

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None: 
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.ante = self.cola   	#faltaba agregar el link al anterior nodo
            self.cola.sgte = nodo
            self.cola = nodo
            #self.cabeza.ante = self.cola
            
        self.size +=1

    def agregar_inicio(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.sgte = self.cabeza  #este siempre es cabeza porque nunca se modifica es asi por que si
            self.cabeza.ante = nodo
            self.cabeza = nodo
        self.size+=1

    def agregar_mitad(self, valor):
        actual = self.cabeza
        nodo = Nodo(valor)
        mitad = self.size//2
        cont=0
        while(cont<mitad):
            actual = actual.sgte
            cont+=1
        nodo.ante = actual.ante
        nodo.sgte = actual
        actual.ante.sgte = nodo
        actual.ante = nodo
        self.size+=1

    def recorrer(self):
        actual = self.cabeza 
        while actual: 
            valor = actual.valor
            actual = actual.sgte 
            yield valor 

    def recorrer_de_atras(self):
        actual = self.cola
        while actual:
            valor = actual.valor
            actual = actual.ante
            yield valor

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.sgte

    def eliminar_numero(self, num):
        while self.cabeza.valor == num:
            self.cabeza.sgte.ante = None
            self.cabeza = self.cabeza.sgte
            self.cant_elim += 1
        
        actual = self.cabeza
        while actual:
            if actual.valor == num:
                actual.sgte.ante = actual.ante
                actual.ante.sgte = actual.sgte
                self.cant_elim += 1
            actual = actual.sgte

        print('cantidad de nodos eliminados: ', self.cant_elim)

    def enteros(self):
        print('los enteros son: ')
        actual = self.cabeza
        while actual:
            if '.' not in str(actual.valor):
                print(actual.valor, end=' ')
            actual = actual.sgte
        
    def promedio(self):
        actual = self.cabeza
        s = 0; b = 0
        while actual:
            s += actual.valor
            b+=1
            actual = actual.sgte
        print('\npromedio: ', s/b)
        return s/b     

    def mayores_prom(self, prom):
        print('\nmayores que el promedio de L1:')
        actual = self.cabeza
        while actual: 
            if actual.valor > prom:
                print(actual.valor, end=' ')
            actual = actual.sgte
            
    def borrar_mayores(self, valor):
        while self.cabeza.valor > valor:
            self.cabeza.sgte.ante = None
            self.cabeza = self.cabeza.sgte
            
        while self.cola.valor > valor:
            self.cola.ante.sgte = None
            self.cola = self.cola.ante
            
        actual = self.cabeza
        
        while actual:
            if actual.valor > valor:
                actual.ante.sgte = actual.sgte
                actual.sgte.ante = actual.ante
            actual = actual.sgte
        

def particular(num):

    print('lista1 con borrados')
    lista1.eliminar_numero(num)
    lista1.mostrar()
    
    print('lista2 con borrados')
    lista2.eliminar_numero(num)
    lista2.mostrar()

def enteros_promedios_mayoresL2():
    print('\nlista1')
    lista1.enteros()
    prom = lista1.promedio()    

    print('\nlista2')
    lista2.enteros()
    lista2.mayores_prom(prom)
    


print('lista1')
lista1 = ListaEnlazadaDoble()
lista1.agregar(7)
lista1.agregar(7)
lista1.agregar(4)
lista1.agregar(8)
lista1.mostrar()
lista1.borrar_mayores(5)
lista1.mostrar()



