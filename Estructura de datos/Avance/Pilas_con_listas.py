# creacion de clase Pila

class Paffi:
	
	# la cola es un vector 
	def __init__(self):
		self.elementos=[]

	def apilar(self, valor):
		self.elementos.append(valor)
		return valor

	def vacia(self):
		return len(self.elementos) == 0
			
	def quitar(self):
		return self.elementos.pop()

	def top(self):
		return self.elementos[-1]



# Implementación de clase Pila

if __name__ == '__main__':
	#creación de objeto pila
	pila = Paffi()

	#Verificando si la pila esta vacia
	print('La pila esta vacia? ',pila.vacia())

	#apilando elementos
	pila.apilar('Sheyla')
	pila.apilar('Nicole')
	pila.apilar('Emiliana')
	pila.apilar('Laura')
	pila.apilar('Jassiel')

	#imprimiendo elementos de la pila	
	print('Integrantes de la pila: ', pila.elementos)

	#verificando si la pila esta vacia
	print('La pila esta vacia? ', pila.vacia())

	#mostrando el top de la pila
	print('Integrante en el top: ', pila.top())

	#quitando elementos de la pila
	print('quitando ultimo integrante la pila: ', pila.top())
	pila.quitar()

	#mostrar ultimo integrante de la pila
	print('Integrante en el top actual: ',pila.top())

	#quitando elementos restantes
	print('quitando integrantes restantes')
	pila.quitar(); pila.quitar(); pila.quitar(); pila.quitar()

	#comprobando si la pila esta vacia
	print('La pila esta vacia? ',pila.vacia())

