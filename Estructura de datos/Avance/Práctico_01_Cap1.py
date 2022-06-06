# -*- coding: utf-8 -*-

# Nro 2 - instrucciones de c++ en python

'''
if(3>7):
	print('Es verdad')
else:
	print('Es mentira')

i = 0; n=7

#########

while(i<=n):
	print('sigue creciendo')
	i+=1

########

def do(a):
	print('el ciclo sigue')
	a+=1
	return a

def until(k, j):
	if(k>j):
		return False
	else:
		return True

k=0; j =7

while(True):
	k = do(k)
	if until(k, j)==False: 
		break

########

c=2; d=5

for c in range (d):
	print('Aumenta el valor')

########

op = int(input("Opcion: "))

if(op=='1'):
	print('Se eligio la opcion 1')
elif(op=='2'):
	print('Se eligio la opcion 2')
elif(op=='3'):
	print('Se eligio la opcion 3')
else:
	print('no existe esa opcion')				#este es el caso default
'''


#																			Nro 4 - Evaluacion de polinomios 

'''
def eval(pol, x):
	s=0
	for exp in pol:
		s+=(x**int(exp))*pol[exp]
		print(s)
	return s

def attach(poly, exp, coef):
    poly[exp]=coef
    return poly

A={}
n = int(input('Nro de elementos: '))
for k in range (n):
	exp=int(input('Exp: '));
	coef=float(input('Coeficiente: '))
	attach(A, exp, coef)

print(A)

x = float(input('Valor para evaluar en polinomio: '))
print('El resultado es: ', eval(A, x))
'''


#																Nro. 5 - Combinaciones de variables booleanas

'''
def comb(vec,i,n):
	if i<n:
		comb(vec, i+1, n)
		vec[i]=not(vec[i])
		comb(vec,i+1, n)
	else:
		print(vec)						# solamente imprime el vector con las modificaciones que se le hace
		
n = int(input('Nro de variables: '))

vec=[None]*n							#sirve para crear los elementos del vector pero en elementos nulos
for i in range(n):
	vec[i]=True							# asigna todos los valores como True

comb(vec,0, n)
'''


#												Nro. 6 - Comparar n^n y 2^n/4 para valores de n. hallar cuando el 2do se hace mas grande

'''
def ver(n):
	a=n**n
	b=(2**n)/4
	print(a,' ',b)
	
	while(b<a):
		n+=0.1
		a=n**2
		b=(2**n)/4
		print(a,' ',b)
		if b>a:
			print('el segundo se hizo mayor que el primero a partir de', n)
			break

n = float(input("Valor de n: "))
ver(n)
'''

#							Nro. 8 -	Buscar x en un arreglo (1:n). si esta en el arreglo entonces j es la posicion de en el arreglo, sino j es cero

'''
def buscar(V, n, x):

	if n==0:
		return 0
	if x==V[n]:
		return n
	else:
		return buscar(V, n-1, x)

V=[]
n = int(input('Valor de n: '))

for i in range (1, n):	
	a = int(input('Elemento'))
	V.append(a)

print(V)
x = int(input('Valor de x: '))
j = buscar(V, n-1, x)
print('El valor de j es ', j)
'''
'''
def buscar(V, n, x, j):

	for k in range (n):
		if x==V[k]:
			print('si hay coincidencia')
			V[k]=j
			break
		if x not in V:
			V.insert(0,j)
			break
			
V=[] 
n = int(input('Valor de n: '))

for i in range (n):	
	a = int(input('Elemento: '))
	V.append(a)

print(V)
x = int(input('Valor de x para buscar: '))
j = int(input('Valor a reemplazar: '))
buscar(V, n, x, j)
print('nuevo vector: ', V)
'''

#											Nro. 9 - concatenar x y y para asignarlo a z / hacer un substring que copia desde i hasta j de un string x  / buscar el primer x en y para asignarlo a z 

'''
def concat(x, y):
	aux = x+y
	return aux

def substr(x, i, j):
	aux='' 
	for k in range (i, j):
		aux+=x[k]
	return aux

def index(x, y):
	n=0
	if y not in x:
		return 0
	else:
		for a in x:
			if y == a:
				return n
			n+=1

x = input('frase: ')
y = input('frase 2: ')
z = concat(x, y); print('concatenado:',z)
'''

# 													Nro. 10 - Eliminar espacios en el string hasta que se reduzca hasta solo un espacio

'''
def reduct(frase):
	n=len(frase)
	FILE=''
	for k in range(n):
		if frase[k]!=' ':
			FILE+=frase[k]
		elif frase[k+1]!=' ':
				FILE+=' '		
	print(FILE)
			
frase = 'abc   def  ccc fff g'
reduct(frase)
'''

#												Nro 11 - Contar las ocurrencias de un caracter en un string de longitud n. Mostrar la respuesta en un arreglo ANS(1:k, 1:2)

'''
def contar(string):
	ans={}
	for k in string:
		ans[k]=0
	print(ans)

	for i in string:
		for k in ans:
			if i == k:
				ans[k]+=1
	for a in ans:
		print(a, ' ',ans[a])
	
	
string = 'mateo es alto'; n=len(string)
contar(string)
'''

##																				Nro 12 - Probar por induccion las sumatorias 

'''
def suma1(n):
	s=n*(n+1)/2
	return s

def suma2(n):
	s=(n*(n+1)*(2*n+1))/6
	return s

def suma3(x, exp):
	s=((x**(exp+1))-1)/(x-1)
	return s


n = int(input('Valor de n: '))
print('suma de naturales: ', suma1(n))
print('suma de cuadrados', suma2(n))
x=float(input('valor de x: '))
print('enesima potencia: ', suma3(x, n))
'''

#																				Nro 13 - Fibonacci con recursividad

'''
def fibo(n):					# el 0 devuelve -1 porque estamos trabajando como si fuera una serie normal y no con posiciones de vector
	if n<=2:
		return n-1
	else:
		return fibo(n-1) + fibo(n-2)

n = int(input('Elemento de la serie fibonacci: '))
print('El elemento', n, 'es: ', fibo(n))
V=[]
for i in range(1, n+1):
	V.append(fibo(i))
print(V)
'''


##																		Nro 14 - MCD y MCM con recursividad y euclides

'''
def mcd(a, b):
	
	maxi=max(a, b)
	mini=min(a, b)
	if mini==0:
		return maxi
	elif mini==1:
		return 1
	else:
		return mcd(mini, maxi%mini)

res = mcd(7,5); print('el mcd es: ', res)

def mcm(a, b):
	return a*b / (mcd(a, b))

res2= mcm(7, 9); print('el mcm es: ', res2)
'''

##														Nro 15 - Desarrollar de forma recursiva las											operaciones aritmeticas de suma, resta, multiplicacion y division.

'''
def suma(a, b):
	if b==0:
		r=a
	elif b<0:							# si b es negativo, lo hace llegar a 0 y va reduciendo a 
		r=suma(a-1, b+1)
	else:
		r=suma(a+1, b-1)				# si b es positivo, lo va reduciendo hasta 0 y va aumentando a
	return r

print('la suma es: ', suma(2, 5))

def multiplica(a, b):
	if b==0:
		r=b
	else:
		r=a+multiplica(a, b-1)				# la multplicacion hecha en base de sumas sucesivas hasta que el multiplicador se hace 0 y devuelve todo las veces que ha sumado a
	return r

print('multiplicacion de 2 y 7 es: ',multiplica(2, 7))

def divide(a, b):
	if b>a:
		r=0
	else:
		r=1+divide(a-b, b)					# devuelve el residuo que aumenta en uno cada vez que detecta que el 2do argumento es divisor del 1ro
	return r

print('divison de 14 y 2 es: ',divide(14, 2))

def potencia(a, b):
	if b==0:
		r=1
	else:
		r=a*potencia(a, b-1)				# va multiplicando el argumento de la izquierda hasta que el de la derecha se hace cero (completa el nro de potencias)
	return r

print('pitencia de 2 a la 3 es: ',potencia(2, 3))
'''



def suma2(a, b):
    maxi=max(a, b)
    mini=min(a, b)
    if maxi==0:
        return mini
    if mini==0:
        return maxi
    if mini>0:
        return suma2(maxi+1, mini-1)
    elif mini<0:
        return suma2(maxi-1, mini+1)
    elif mini<0 and maxi<0:
            mini*=-1; maxi*=-1
            return suma2(maxi-1, mini+1)
        
fin2 = suma2(-1, 0); print(fin2)
fin1 = suma2(3, 0); print(fin1)
fin3 = suma2(-1, 3); print(fin3)
fin4 = suma2(2,7); print(fin4)
fin5 = suma2(-9,-1); print(fin5)