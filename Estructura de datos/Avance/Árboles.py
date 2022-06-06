# crear una clase para la busqueda binaria

class Nodo:
	def __init__(self, valor):
		self.izq = None 
		self.der = None
		self.valor = valor

def insertarArbolBinario(raiz, nodo):
	if raiz is None:
		raiz = nodo

	else:
		if raiz.valor > nodo.valor:
			if raiz.izq == None:
				raiz.izq  = nodo
			else:
				insertarArbolBinario(raiz.izq, nodo)
		else:
			if raiz.der is None:
				raiz.der = nodo
			else:
				insertarArbolBinario(raiz.der, nodo)

def inorden(raiz):
	if raiz is not None:
		inorden(raiz.izq)
		print(raiz.valor)
		inorden(raiz.der)

def posorden(raiz):
	if raiz is not None:
		posorden(raiz.izq)
		if raiz.izq is None and raiz.der is None:
			print(raiz.valor)
		if raiz.izq is not None and raiz.der is not None:	
			posorden(raiz.der)
			print(raiz.valor)

def preorden(raiz):
	if raiz is not None:
		print(raiz.valor)
		preorden(raiz.izq)
		preorden(raiz.der)

def buscar(raiz, x):
	if raiz is None:
		return False
	elif x == raiz.valor:
		return True
	elif x < raiz.valor:
		return buscar(raiz.izq, x)
	else:
		return buscar(raiz.der, x)

	
raiz = Nodo(21)
insertarArbolBinario(raiz, Nodo(13))
insertarArbolBinario(raiz, Nodo(10))
insertarArbolBinario(raiz, Nodo(33))
insertarArbolBinario(raiz, Nodo(18))
insertarArbolBinario(raiz, Nodo(25))
insertarArbolBinario(raiz, Nodo(40))

inorden(raiz); print('\n')
posorden(raiz); print('\n')
preorden(raiz); print('\n')
x = int(input('Valor a buscar en arbol: '))
print(buscar(raiz, x))