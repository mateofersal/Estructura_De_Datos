from collections import deque		#deque provee herramientas para manejar colas como si crearamos una clase Cola
	
#creando un objeto cola

cola = deque()

#verificando si la cola esta vacia
print(len(cola)== 0)

#metiendo elementos a la cola
cola.append(5)
cola.append(6)
cola.append(5)
cola.append(7)
cola.append(10)

# verificando si la cola esta vacia
print(len(cola)== 0)

# mostrando cola
print(cola)

#sacando elementos de la cola
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()

#verificando si la cola esta vacia
print(len(cola)== 0)