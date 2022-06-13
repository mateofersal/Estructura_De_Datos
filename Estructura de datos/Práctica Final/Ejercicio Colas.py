class ColaDePostulantes:
    def __init__(self):
        self.postulantes = []
    
    def nuevo_postulante(self, nombre):
        self.postulantes.append(nombre)
    
    def proximo_postulante(self):
        return self.postulantes.pop(0)

    def lleno(self):
        return len(self.postulantes)!=0

    def mostrar(self):
        for k in self.postulantes:
            print(k, end='\n')
    
class Entrevista:
    def __init__(self):
        self.lista=[]
        self.oficinas = {}

    def nuevo_postulante(self, entrevistador, oficina):
        aux= []
        aux.append(cola.proximo_postulante())
        aux.append(entrevistador)
        aux.append(oficina)
        self.lista.append(aux)
        aux=[]

    def mostrar(self):
        for k in self.lista:
            print(k, end= '\n')


    def abrir_oficinas(self):
        
        for k in self.lista:
            self.oficinas[k[2]] = []
        
        print('\nAbriendo oficinas')
        for k in self.oficinas:
            print('Oficina', k, ': Vacio')

        print('\nEncolando personas en sus oficinas: ')
        for k in self.lista:
            for of in self.oficinas:
                if k[2]==of:
                    self.oficinas[of].append(k[0])

        for k in self.oficinas:
            print('Oficina' ,k ,':' ,  self.oficinas[k], end='\n')


    def proximo_postulante(self):
        
        print('\nEntrevistando')
        for of in self.oficinas: 
            if len(self.oficinas[of])!=0:
                print('Oficina',of,'atendiendo a: ',self.oficinas[of][0] )
                self.oficinas[of].pop(0)
            else:
                print('Oficina',of,'ahora vacia')


print('Entrando a la sala de espera: ')


# creacion de cola de postulantes
cola = ColaDePostulantes()
cola.nuevo_postulante('mateo')
cola.nuevo_postulante('emi')
cola.nuevo_postulante('luis')
cola.nuevo_postulante('rafael')
cola.mostrar()

# creacion de sala de entrevista
sala = Entrevista()
print('\nEntrevistadores y oficinas')

while cola.lleno():
    
    print(cola.postulantes[0])
    ent = input('entrevistador: ')
    of = input('oficina: ')
    sala.nuevo_postulante(ent, of); print(' ')

sala.mostrar()
sala.abrir_oficinas()
sala.proximo_postulante()
sala.proximo_postulante()



        

