fp = open('D:\Códigos\Códigos Python\Proyecto Final\lista_tareas.txt', 'w+')

class Lista():
    def __init__(self):
        self.elementos = []

    def agregar(self, valor):
        self.elementos.append(valor)


lista = Lista()
lista.agregar('hacer comida')
lista.agregar('cemar')
lista.agregar('hacer jugo')

for e in lista.elementos:
    fp.write('%s\n' % e)

fp.close()