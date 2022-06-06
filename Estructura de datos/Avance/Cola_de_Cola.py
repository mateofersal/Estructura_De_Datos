from queue import Queue

#crear un objeto cola
cola_obj = Queue()

#verificando si la cola esta vacia
print(cola_obj.empty())

#metiendo elementos a la cola
cola_obj.put(3)
cola_obj.put(7)
cola_obj.put(3)
cola_obj.put(4)
cola_obj.put(10)

#verificando si la cola esta vacia
print(cola_obj.empty())

#mostrando elementos 
print(cola_obj.queue)		#muestra elementos de una cola 

#mostrando el tamaño de la cola
print('El tamano de la cola es: ', cola_obj.qsize())

#sacar los elementos de la cola
cola_obj.get()
cola_obj.get()
cola_obj.get()
cola_obj.get()
cola_obj.get()

# verificando si la cola esta vacia
print(cola_obj.empty())