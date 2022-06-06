from queue import Empty, PriorityQueue

# creacion de una clase para
class Curso:
	def __init__(self, prioridad, nombre):
		self.prioridad = prioridad
		self.nombre = nombre
	
	# metodo de comparacion de prioridades (necesario para el priority queue)
	def __lt__(self, other):
		return self.prioridad < other.prioridad
		


# implementación la cola de prioridad
cursos  = PriorityQueue()

#agregar elementos a la cola de prioridad
cursos.put(Curso(4, 'Jassiel'))
cursos.put(Curso(3, 'Mateo'))
cursos.put(Curso(1, 'Emiliana'))
cursos.put(Curso(5, 'Ana'))
cursos.put(Curso(2, 'Lucas'))

# mostar los elementos de la cola de prioridad-+
while not cursos.empty():
	c = cursos.get()
	print(c.prioridad, c.nombre)
