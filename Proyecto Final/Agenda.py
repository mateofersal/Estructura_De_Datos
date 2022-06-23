import datetime
import locale
import os 
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)
locale.setlocale(locale.LC_ALL, 'es-ES')

# Guia para trabajar con mes y dia

hoy = datetime.datetime.now()
mes = str(hoy.strftime('%B'))
dia = str(hoy.day)
año = str(hoy.year)
hora = str(hoy.strftime("%X"))

actual = mes + ' ' + dia
todo = actual + ' ' + año + ' ' + hora

meses = {   'enero': 1,
            'febrero': 2,
            'marzo': 3,
            'abril': 4,
            'mayo': 5,
            'junio': 6,
            'julio': 7,
            'agosto': 8,
            'septiembre': 9,
            'octubre': 10,
            'noviembre': 11,
            'diciembre': 12
        }

class Nodo:
    def __init__(self, valor, contenido):
        self.izq = None
        self.der = None
        self.valor = valor
        self.contenido = contenido

class Agenda():

    def __init__(self):
        self.T = []
        self.E = {}

    def agregar_tarea(self):   

        print('-------', Fore.CYAN + todo,'-------\n')
        tarea = input('     ¿Cual es la tarea para añadir?: ')
        self.T.append(tarea)
        show = buscarelemento(raiz, 1)
        print(show)
        
    def mostrar_tareas(self):

        print('______________________________________\n')
        time.sleep(0.2)
        print('\n       Tareas para hoy ', Fore.LIGHTGREEN_EX + actual, '\n')
        time.sleep(0.2)
        print('______________________________________\n')
        if len(self.T) ==0:
            print(' .........Todavia no hay tareas agendadas.........\n')
            print(' .......Vuelve al inicio y añade una tarea........\n')
        else:
            for k in range(len(self.T)):
                time.sleep(0.5)
                print(k+1,'.', self.T[k])
    
    def eliminar_tarea(self):

        self.mostrar_tareas()
        if len(self.T)!=0:
            numero = int(input('\nNro de tarea a eliminar: '))
            for k in range(len(self.T)):
                if k==numero-1:
                    self.T.pop(k)
                show = buscarelemento(raiz, 3)
            print(show)
                
    def agregar_evento(self):

        mes = input('Mes: '); mes = mes.lower()
        dia = int(input('Dia: '))
        key = mes + ' ' + str(dia)
        evento = input('\nEvento para agendar: ')
        for k in meses:
            if mes == k:
                valor = meses[k]

        valor *= 100
        valor += dia
        self.E[key]=[]
        self.E[key].append(valor)
        self.E[key].append(evento)
        show = buscarelemento(raiz, 12)
        print(show)
    
    def mostrar_eventos(self):

        print('_____________________________________\n')
        time.sleep(0.2)
        print('\n         Eventos agregados \n')
        time.sleep(0.2)
        print('_____________________________________\n')
        V = sorted(self.E.items(), key = lambda t: t[1])    # se hace sorting previo al reinicio del diccionario
        self.E={}       # se debe reiniciar el diccionario para poderle meter todo ordenado
        for e in V:
           self.E[e[0]] = e[1]

        if self.E == {}:
            print(' ......... Todavia no hay eventos agendados .........\n')
            print(' ........ Vuelve al inicio y añade un evento ........\n')
        
        for k in self.E:
            time.sleep(0.5)
            print(Fore.YELLOW + k, end='')
            print(': ',self.E[k][1])

    def eliminar_evento(self):
    
        self.mostrar_eventos()
        if self.E != {}:
            print('\nIngrese la fecha del evento a ser borrado\n')
            mes = input('Mes: ')
            dia = int(input('Dia: '))
            borrar = mes + ' ' + str(dia)
            if borrar in self.E:
            
                del self.E[borrar]
                show = buscarelemento(raiz, 19)
                print(show)
            else:   
                print('  ¡ ¡ ¡ Esta fecha no tiene eventos agregados ! ! !')

    def editar_evento(self):

        self.mostrar_eventos()
        if self.E != {}:
            print('\n¿Que evento desea modificar? ')
            mes = input('\nMes: ')
            dia = int(input('Dia: '))
            editar = mes + ' ' + str(dia)
            if editar in self.E:
                evento = input('\n\nReescriba su evento: ')
                self.E[editar][1]=evento
                show = buscarelemento(raiz, 15)
                print(show)
            else:
                print('  ¡ ¡ ¡ Esta fecha no tiene eventos agregados ! ! !')

def insertarArbolBinario(raiz, nodo):

        if raiz is None:
            raiz = nodo
        else: 
            if raiz.valor > nodo.valor:
                if raiz.izq is None:
                    raiz.izq = nodo

                else:
                    insertarArbolBinario(raiz.izq, nodo)
            else: 
                if raiz.der is None:
                    raiz.der = nodo

                else: 
                    insertarArbolBinario(raiz.der, nodo)

def buscarelemento(raiz,x):
    if raiz is None:
        return False
    elif x == raiz.valor:
        return raiz.contenido
    elif x < raiz.valor:
        return buscarelemento(raiz.izq,x) 
    else: 
        return  buscarelemento(raiz.der,x) 


# Creacion del arbol de decisiones

raiz = Nodo(10,'\n                    1. Tareas \n\n                    2. Eventos \n\n                    3. Mostrar')

# lado izquierdo del arbol (tareas)
insertarArbolBinario(raiz, Nodo(7,'          1. Crear tarea \n\n          2. Eliminar tarea '))
insertarArbolBinario(raiz, Nodo(1, Fore.GREEN + '\n          [Tarea añadida]'))
insertarArbolBinario(raiz, Nodo(3, Fore.LIGHTRED_EX + '\n\n  |   Tarea eliminada   |'))

#lado derecho del arbol (eventos)
insertarArbolBinario(raiz, Nodo(14,'           1. Agregar evento\n\n           2. Modificar evento'))
insertarArbolBinario(raiz, Nodo(12, Fore.GREEN + '\n      [Evento añadido]'))
insertarArbolBinario(raiz, Nodo(17, '           1. Editar evento \n\n           2. Eliminar evento '))
insertarArbolBinario(raiz, Nodo(15, Fore.MAGENTA + '\n\n |   Evento reescrito  |'))
insertarArbolBinario(raiz, Nodo(19, Fore.LIGHTRED_EX + '\n\n |   Evento eliminado   |'))

agenda = Agenda()

def organizador():
    
    opcion = 'si'

    while(opcion == 'si'):

        print('\n                    ¿Que desea hacer?')
        print(raiz.contenido)
        select = int(input('\nSelección: ')); os.system('cls')

        if select == 1:

            os.system('cls')
            show = buscarelemento(raiz, 7); print(show)
            aux = input('\nSeleccion: '); os.system('cls')
            
            if aux == '1':
                agenda.agregar_tarea()
                
            if aux == '2':
                agenda.eliminar_tarea()

            if aux == 'A':
                select = ''
        
        if select == 3:
    
            print('          1. Mostrar tareas \n\n          2. Mostrar eventos ')
            aux = input('\nSeleccion: '); os.system('cls')

            if aux == '1':
                agenda.mostrar_tareas()

            if aux == '2':
                agenda.mostrar_eventos()

            if aux == 'A':
                select = ''

        if select == 2:

            show = buscarelemento(raiz, 14); print(show)
            aux = input('\nSeleccion: '); os.system('cls')

            if aux == '1':
                agenda.agregar_evento()
            
            if aux == '2':

                show = buscarelemento(raiz, 17); print(show)
                sub_aux = input('\nSeleccion: '); os.system('cls')
                
                if sub_aux == '1': 
                    agenda.editar_evento()
            
                if sub_aux == '2':
                    agenda.eliminar_evento()

            if aux == 'A':
                select = ''

        opcion = input('\n\nDesea continuar con su agenda?:  ')
        os.system('cls')

    print('              Fue un gusto ayudarte a organizar tu día:)                \n')

print(Fore.CYAN + '_________________________________________________________\n')
print('           BIENVENIDO A SU AGENDA PERSONAL 2022           ')
print(Fore.CYAN + '_________________________________________________________')

organizador()