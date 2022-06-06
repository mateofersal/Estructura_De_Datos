#PILAS

def crear():
	global S, top
	S=[]
	top=0

def crear_2():
	n = int(input('Nro de elementos: '))
	S=[None]*n
	global top
	top=0
	return S, top

def add(S, n, top):
	if top>=n:
		stack_full()
	else:
		top+=1
		x = int(input('Elemento a apilar: '))
		S.append(x)
		print(S)	
	return top

def stack_full():
	print('Full')

def delete(S, top):					
	b = S.pop(top-1)
	print('\nElemento borrado: ', b)
	top-=1
	return top

def show_top(S, top):
	print (S[top-1])

def isempt(S, top):
	if top == 0:
		return False
	else:
		return True


n = int(input('Nro de elementos a apilar: '))
crear()
print('\nApilando datos')
top=add(S, n, top)
top=add(S, n, top)
top=add(S, n, top)
top=add(S, n, top)
top=add(S, n, top)

print('\nBorrando el top de la pila', end=''); top=delete(S, top); print('Cola actual: ',S, end=''); 
print('\n\nEl elemento por encima de la pila es: ', end=''); show_top(S, top)
print('\nTrue: Pila con datos / False: pila sin datos:'); print(isempt(S, top))  


#COLAS

#def crear():
#	S=[]
#	front=0
#	rear=0
#	return S,front,rear

#def add(C, n, x, rear):
#	front=0
#	if rear>=n:
#		front=1
#		queue_full()
#		return front, rear
#	else:
#		front=1
#		rear+=1
#		C.append(x)
#		print(C)
#		return front, rear
	

#def queue_full():
#	print('Cola Full')

#def delete(C, rear):					
#	rear-=1
#	front=0
#	C.pop(0)
#	if rear==0:
#		return front, rear
#	else:
#		front=1
#		return front, rear
	

#def show_front(C):
#	print (C[0])

#def isempt(C, rear):
#	if  rear==0:
#		return False
#	else:
#		return True

#C, front, rear = crear()
#print('Sin elementos ')
#print('front: ', front); print('rear: ', rear)
#n = int(input('\nNro de elementos: '))
#front,rear=add(C, n, 1, rear);print(end=''); print('front: ', front,'rear: ', rear)
#front,rear=add(C, n, 2, rear); print('front: ', front,'rear: ', rear)
#front,rear=add(C, n, 3, rear); print('front: ', front,'rear: ', rear)
#front,rear=add(C, n, 4, rear); print('front: ', front,'rear: ', rear)
#front,rear=add(C, n, 5, rear); print('front: ', front,'rear: ', rear)
#print('\n-----------')

#print('\nEliminando el front'); front, rear=delete(C, rear); print(C);  print('front: ', front,'rear: ', rear)
#print('\nEliminando el front'); front, rear=delete(C, rear); print(C);  print('front: ', front,'rear: ', rear)
#print('\nEliminando el front'); front, rear=delete(C, rear); print(C);  print('front: ', front,'rear: ', rear)
##print('\nMostrando el front: ', end=''); show_front(C);
#print('\nPila con elementos? ', end=''); print(isempt(C, rear))
