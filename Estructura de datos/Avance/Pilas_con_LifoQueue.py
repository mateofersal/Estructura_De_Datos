from queue import LifoQueue

#crear objeto pila

pila = LifoQueue()

#ver si la pila esta vacia
print(pila.empty())

#añadiendo elementos a la pila
print('apilando')
pila.put(3)
pila.put(6)
pila.put(7)
pila.put(1)
pila.put(2)

#ver si la pila esta vacia
print(pila.empty())

#mostrar pila
print(pila.queue)

#desapilar elementos
print('quitando elementos de la pila')
pila.get(); pila.get();pila.get();pila.get();pila.get()

#ver si la pila esta vacia
print(pila.empty())