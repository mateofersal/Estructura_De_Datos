class Paciente:
    def __init__(self, nombre, doc):
        self.nombre = nombre
        self.doc = doc

    def __str__(self):
        return self.nombre + ' - ' + self.doc

class ColaDePacientes:
    def __init__(self):
        self.espera = []    
        self.size = 0

    def nuevo_paciente(self, nombre, doc):
        paciente = Paciente(nombre, doc)
        self.espera.append(paciente)
    
    def proximo_paciente(self): 
        print('proximo paciente: ',self.espera[self.size])
        self.size+=1
    
    def mostrar(self):
        for k in self.espera:
            print(k.nombre, ' - ', k.doc)

class Recepcion:
    def __init__(self):
        self.consultorios={}

    def nuevo_paciente(self, cola):
        for k in cola.espera:
            self.consultorios[k.doc]=[]
        
        print('\nAbriendo consultorios\n')
        for k in self.consultorios:
            print(k, ':  Vacio\n')

        for doctor in self.consultorios:
            for k in cola.espera:
                if doctor == k.doc: 
                    self.consultorios[doctor].append(k.nombre)
        
        print('\nEncolando pacientes con su doctor: \n')
        for k in self.consultorios:
            print(k, ': ',end = '')
            print( self.consultorios[k], '\n')
        
    def proximo_paciente(self):
        print('\nAtencion del proximo paciente: \n')
            
        for k in self.consultorios:
                if len(self.consultorios[k]) != 0:
                    print('Atencion de: ', self.consultorios[k][0])
                    self.consultorios[k].pop(0)

cola_recepcion = ColaDePacientes()
print('\nRecepcion de pacientes: \n')
cola_recepcion.nuevo_paciente('Mateo', 'Traumatologo')
cola_recepcion.nuevo_paciente('Pedro', 'Oftalmologo')
cola_recepcion.nuevo_paciente('Emi', 'Ginecologo')
cola_recepcion.nuevo_paciente('Maria', 'Traumatologo')
cola_recepcion.nuevo_paciente('Lucas', 'Oftalmologo')

cola_recepcion.mostrar()

print('\nPaso de pacientes: \n')
cola_recepcion.proximo_paciente()
cola_recepcion.proximo_paciente()
cola_recepcion.proximo_paciente()
cola_recepcion.proximo_paciente()
cola_recepcion.proximo_paciente()

cola_consultorios = Recepcion()
cola_consultorios.nuevo_paciente(cola_recepcion)
cola_consultorios.proximo_paciente()
cola_consultorios.proximo_paciente()






