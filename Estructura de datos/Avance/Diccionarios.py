# -*- coding: utf-8 -*-
#P = {'80': -3.6, '75':12, '70':-1, '2':4.6, '1':1}		#el indice siempre debe ir acompañado de su valor
#print(P)

#for i in P:
#	print(i, P[i])		#Imprime los valores indices (lo que esta en comillas) 
#   						# P[i] es el valor del indice 
#print(len(P))			# Imprime el numero de indices del diccionario

#n=int(input('n para nro de elementos: '))
#aux=0
#for i in P:
#	print(i, P[i])
#	if aux>n:
#		break
#	aux+=1
'''
def zero():
	poly={}
	return poly

def coef(poly, exp):
	return poly[exp]

P = {'80': -3.6, '75':12, '70':-1, '2':4.6, '1':1}

print(zero())
print(P)
print(coef(P, '75'))
'''

'''
def meter(V, n):
	for k in range (n):
		expo=input('expo: ')
		coef=int(input('coef: '))
		V[expo]=0
		V[expo]=coef

	return V

def suma(P,Q,R):
	
	for k in P:					# crear un diccionario en 0
		R[k]=0
	for i in Q:
		R[i]=0

	for c in R:							
		for k in P:
			if k==c:
				R[c]+=P[k]
	for c in R:
		for i in Q:
			if c==i:
				R[c]+=Q[i]	

	print(R)


P={}; Q={}; R={}
meter(P, 3); print(P)
meter(Q, 2); print(Q)
suma(P,Q,R)
'''

P={}

for k in range (10):
	P[k]

print(P)
