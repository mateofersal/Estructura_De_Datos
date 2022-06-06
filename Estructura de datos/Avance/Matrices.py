# -*- coding: utf-8 -*-
# Creacion de Matriz

def crear(M):
	aux=[]
	f = int(input('Nro de filas: '))
	c = int(input('Nro de columnas: '))
	for k in range (f):
		for i in range (c):
			e = int(input(''))
			aux.append(e)		#metemos los elementos de una fila
		print('-----')
		M.append(aux)			#añade la primer fila a la matriz
		aux=[]	#reinicia la fila
	l = len(M)	#el tamaño de la matriz es el nro de filas.
	
	for k in range (l):		#imprime la matriz como vector con elementos que son vectores
		print(M[k])

	#for f in range(len(M)):
	#	for c in range(len(M[0])):  #lenM[0]-> tamaño de fila (nro columnas)
	#		print(M[f][c], end=' ')
	#	print('\n', end='')	

def show_mat(M):
	for k in range (len(M)):
		print(M[k])

def elemento(M, f, c):
	return M[f][c]

def tam(M):
	print('\nEl tamano de la matriz es ', len(M),'x', len(M[0]))

def mult_elem(M, f, x):
	for k in range(len(M)):
		if k == f:								
			for i in range(len(M[0])):			
				M[k][i]*=x
			break
	return M

#def perm_elem()

#def suma_elem()

def suma(A, B):
	C=[]; aux=[]
	if len(A) != len(B) or len(A[0]) != len(B[0]):
		print('\nNo se puede sumar')
	else: 
		print('\nLa matriz suma es: \n')
		for k in range(len(A)):
			for i in range (len(A[0])):
				e = A[k][i]+B[k][i]
				aux.append(e)
			C.append(aux)
			aux=[]

		#for j in range(len(A[0])):
		#	for k in range (len(A[0])):
	return C

def mult(A, B):
	C=[]; aux=[]; e=0
	for f in range (len(A)):
		for c in range (len(B[0])):
			for k in range(len(A[0])):
				e += A[f][k]*B[k][c]			
			aux.append(e)
			e=0
		C.append(aux)
		aux=[]
	return C

M1=[]; M2=[]; M3=[]
crear(M1)
crear(M2)
M3 = mult(M1, M2); print('Matriz resultado: '); show_mat(M3)

#tam(M1)

#print('\nElemento a buscar: '); 
#fil=int(input()); col=int(input())
#print('Elemento en posicion [',fil,',',col,'] es:', elemento(M1, fil-1, col-1)) 

#print('\nFila para multiplicacion: ', end='')
#fila_m = int(input()); 
#x = int(input('Valor para multiplicar: '))
#M1 = mult_elem(M1, fila_m-1, x);
#print('La matriz con fila multiplicada es: ')
#for k in range (len(M1)):		
#		print(M1[k])

