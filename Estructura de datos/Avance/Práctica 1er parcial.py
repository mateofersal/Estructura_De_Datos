from typing import DefaultDict


def zero():         #crea el polinomio (diccionario)
    poly={}
    return poly
    
def expo(poly, exp):    #devuelve el exponente
    return exp

def attach(poly, coef, exp):
    poly[int(exp)]=coef
    return poly
    
def rem(poly, exp):     #elimina un elemento
    del poly[exp]
    return poly    
    
def cargar(poly, n):
    for x in range(n):
        expo=input('Exponente: ')
        coef=float(input('Coeficiente: '))
        poly[expo]=coef
    return poly
    
def imprimir(poly, n):
    print('Expo y coef')
    for c in poly:
        print(c, poly[c], end=',  ')
        
def calc(poly, x):
    s=0
    for exp in poly:
        s+= (x**int(exp))*poly[exp]
    return s

def coef(poly, exp):	#imprime el coeficiente
	return poly[exp]

def vec(poly):
	A=[]
	for e in poly:
		A.append(e)
	return A

def buscar(poly, exp):
	for i in poly:
		if i==exp:
			print('si esta en el polinomio y es', poly[i])




			
											###################################################################

def llenar(P, n):
	for k in range(n):
		e = int(input('expo: '))
		c = int(input('coef: '))
		P[e]=c
	return P

#P={}
#n = int(input('valor de n: ')); P = llenar(P, 3); print(P)
#del P[0]; print(P)


P={}

def nombres(N, n):
	D={}
	for k in range(n):
		#
		nom = input('Nombre: ')
		ap = input('apellido: ')
		D['apellido:']=ap
		ed=int(input('edad: '))
		D['edad:']=ed
		N[nom]=D
		D={}


	for i in N:
		for j in N[i]:
			print( j['edad'])

	return N

P = nombres(P, 2); print(P)



# verificar si la potencia 3 esta en el polinomio, imprimir su coeficiente

#buscar(P, '3')

# imprimir en un vector todas las potencias de P(x)
#A=[]
#A= vec(P); print(A)

# contar el nro de letras en un texto

#frase = 'esto es una prueba'

#def contar(frase):
#	L={}
#	for k in frase:
#		L[k]=0
	
#	for c in frase:
#		for k in L:
#			if c==k:
#				L[k]+=1
#	print(L)
		
	
#contar(frase)

#p={}
#for letra in frase:
#    p[letra]=0

#for letra in p:
#	for word in frase:
#		if letra==word:
#			p[letra]+= 1
#print(p)






