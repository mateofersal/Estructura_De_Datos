# creacion de la clase cola para el correo

class Cliente():
    def __init__(self,cantidad, nombre):
        self.cantidad = cantidad
        self.nombre = nombre

class Cola_correo():
    def __init__(self):
        self.lista = []

    # trabajar con colas circulares
    def encolar(self, cantidad,nombre):
        cliente = Cliente(cantidad,nombre)
        self.lista.append(cliente)
        
    def mostrar(self):
        for k in self.lista:
            print(k.nombre,' ',k.cantidad)
           
    def entregar(self):
        print('cola inicial')
        self.mostrar(); print('\n')
        while len(self.lista)!=0:
            persona = self.lista[0]
            a = persona.cantidad
            if a <= 5:
                persona.cantidad -=a
            else:
                persona.cantidad -= 5
            print('\nentregando cartas')
            self.mostrar()
            if persona.cantidad > 0:
                self.lista.pop(0)
                self.lista.append(persona)
            else:
                self.lista.pop(0)
                print('             entregado total')
            print('\nsiguiente cola')
            self.mostrar(); print('\n')
        print('no hay mas cartas por entregar\n')

cola = Cola_correo()
cola.encolar(3, 'Mateo')
cola.encolar(7, 'Emi')
cola.encolar(10, 'Jose')
cola.encolar(4, 'Pepe')
cola.encolar(9, 'Maria')
cola.entregar()


