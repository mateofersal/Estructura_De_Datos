from collections import deque
	
#creamos el objeto pila

pila = deque()

#verificar si la pila esta vacia
print(len(pila)== 0)

#apilando elementos
pila.append(2)
pila.append(5)
pila.append(8)
pila.append(7)
pila.append(4)

#verificando si la pila esta vacia
print(len(pila)== 0)

#mostrando la pila
print(pila)

#sacando elementos de la pila
print('sacando el primer elemento de la pila')
pila.pop()
print(pila)

#sacando todos los elementos de la pila
print('sacando elementos restantes')
pila.pop()
pila.pop()
pila.pop()
pila.pop()
print(pila)

#verificar si la pila esta vacia
print(len(pila)==0)