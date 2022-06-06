													# Creación de una clase Cola

class Cola:
	
	# la cola es un vector 
	def __init__(self):
		self.elementos=[]

	def encolar(self, valor):
		self.elementos.append(valor)
		return valor

	def vacia(self):
		return len(self.elementos) == 0
			
	def quitar(self):
		return self.elementos.pop()

	def ultimo(self):
		return self.elementos[-1]

	def primero(self):
		return self.elementos[0]

# Implementación de la clase Cola

# habilitando un espacio de nombres
if __name__ == '__main__':
	cola = Cola()
	
	# verificando si la cola esta vacia en su estado inicial
	print(cola.vacia())

	# encolando elementos
	cola.encolar(18)
	cola.encolar(5)
	cola.encolar(4)
	cola.encolar(8)
	cola.encolar(10)

	# imprimiendo la cola
	print(cola.elementos)

	# verificando si la cola esta vacia una vez añadidos los elementos
	print(cola.vacia())

	# imprimiendo el primer y ultimo elemento de la cola
	print('El primer elemento es: ', cola.primero())
	print('El ultimo elemento es: ', cola.ultimo())

	#quitando elementos de la cola
	print('quitando tres elementos')
	cola.quitar(); cola.quitar(); cola.quitar()
	
	#mostrando los elementos que quedan
	print(cola.elementos)

	#quitando todos los elementos restantes
	print('quitando elementos restantes')
	cola.quitar(); cola.quitar()

	#verificando si la cola ha quedado vacia
	print(cola.vacia())


															