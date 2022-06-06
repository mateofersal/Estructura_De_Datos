from queue import PriorityQueue

estudiantes = PriorityQueue()

estudiantes.put((1, 'A'))
estudiantes.put((4, 'D'))
estudiantes.put((5, 'E'))
estudiantes.put((7, 'G'))
estudiantes.put((3, 'C'))

while not estudiantes.empty():
	print(estudiantes.get())