# -*- coding: utf-8 -*-

                                                #Ejercicio 1
                            #Obtener el valor máximo de una lista de elementos

#'''
#A=[]
#print('Digite el valor de n: ', end='')
#n = int(input())

#for i in range (n): 
#    vec = float(input())                # la variable vec es la que recibe los valores digitados
#    A.append(vec)                       # Append se usa para añadir elementos a la lista del vector A[]

#mayor = A[0]

#for k in range(n):
#    if A[k] > mayor:
#        mayor = A[k]

#print('El mayor es: ', mayor)
#'''
                                                   


                                                # Ejercicio 2
                                # Obtener el promedio de valores de un vector


'''
A=[]
print('Digite el valor de n: ', end='')
n = int(input())
s = 0

for i in range(n):
    vec = float(input())
    A.append(vec)
    s += vec

prom = s/n

#print('El promedio de los valores es: ', prom)
'''
                        


                                         # Ejercicio 3
                        # Revertir el orden de una lista en otra lista nueva (mantener la original)


'''
A=[]
B=[]
print('Digite el valor de n: ', end='')
n = int(input())

for i in range (n):
    vec = int(input())
    A.append(vec)
    B.append(vec)

B.reverse()         #funcion para invertir orden
print(A)
print(B)
'''


                                            # Ejercicio 4 
                                   # Generar numeros aleatorios (No se)





                                             #Ejercicio 5
                                    # Determinar si un vector es capicua 

'''
A=[]
B=[]
print('Digite el valor de n: ', end='')
n = int(input())

for i in range (n):
    vec = int(input())
    A.append(vec)
    B.append(vec)

B.reverse()

if A != B:
    print('No es
    
     capicua') 
else: 
    print('Es capicua')
'''


                                       # Ejercicio 6
                                # Dado un vector obtener la maxima diferencia entre elementos consecutivos 


'''
A=[]
print('Digite el valor de n: ', end='')
n = int(input())

for i in range (n): 
    vec = float(input())                
    A.append(vec)

maxima = A[0] - A[1]

for k in range (1, n-2):
    if A[k] - A[k+1] > maxima:
       maxima = A[i] - A[k+1]

print('La maxima diferencia es: ', maxima)
'''

        
                                        # Ejercicio 7
                                # Concatenar dos vectores de tamaño n y m, primero elementos del 1er vec y luego del 2do

'''
A=[]
B=[]
C=[]
print('Digite el valor de n: ', end='')
n = int(input())
print('Digite el valor de m ', end='')
m = int(input())

print('Valores primer vec: ')
for i in range (n):
    vec = int(input())
    A.append(vec)

print('Valores segundo vec: ')
for i in range (m):
    vec = int(input())
    B.append(vec)	

print(A)
print(B)
A.extend(B)
print('Vector concatenado: ',A)
'''


                                # Ejercicio 8
                           # Contar el numero de elementos negativos, positivos y ceros en un vector


'''
n = int(input("Nro de elementos: "))
A=[]
contcero = 0;contpos = 0;contneg = 0

for i in range (n):
    vec = int(input())
    A.append(vec)
    if vec == 0:
        contcero+=1
    if vec > 0:
        contpos+=1
    if vec < 0:
        contneg+=1

print(A)
print('\nTotal de ceros: ',contcero)
print('Total de positivos: ',contpos)
print('Total de negativos: ',contneg)
'''


                                    # Ejercicio 9 (algoritmo desarrollado)
                               # Ordenar una lista de forma ascendente y descendente


'''
def men_may (V, n):

	aux = 0
	for i in range (n):
		for k in range (n-1):
			if V[k] > V[k+1]:
				aux = A[k]
				V[k] = V[k+1]
				V[k+1] = aux

def may_men (V, n):

	aux=0 
	for i in range(n):
		for k in range(n-1):
			if V[k] < V[k+1]:
				aux=V[k]
				V[k]=V[k+1]
				V[k+1]=aux
	
	
A=[]
n = int(input("Nro de elementos: "))

for i in range (n):
	vec = int(input())
	A.append(vec)

print('Vector original: ',A,'\n')
men_may(A, n); print('Vector menor a mayor: ', A, '\n')
may_men(A, n); print('Vector mayor a menor: ', A, '\n')
'''



										# Ejercicio 9 (con funciones)
                               # Ordenar una lista de forma ascendente y descendente
'''
A=[]
n = int(input("Nro de elementos: "))

for i in range (n):
	vec = int(input())
	A.append(vec)

print('Vector original', A, '\n')
A.sort(); print('Vector menor a mayor: ', A, '\n')
A.sort(reverse=True); print('Vector mayor a menor: ', A, '\n')
'''



											# Ejercicio 10 
									# Generar los primeros n numeros de Fibonacci en un vector [1,1,2,3,5,8,13...]

'''
def fibo(V, n):
	
	a=1 
	b=0
	c=0
	for i in range (1,n+1):
		b=a 
		a=c
		c=a+b
		V.append(c)

A=[]
n = int(input("Numero n para serie Fibonacci: "))
fibo(A, n)
print('La serie de Fibonacci hasta el valor', n, 'es: ', A)
'''


															# STRINGS
														
															# Ejercicio 1
												# Convertir a mayuscula todos los caracteres
'''
frase=input("Frase: ")
frase=frase.upper()
print(frase)
'''
														# Ejercicio 2
												# Determinar cuantas palabras existen en una frase

'''
frase = input("Frase: ")
cont = frase.count(" ")
print('El total de palabra es: ',cont +1)
'''


#														 Ejercicio 3
#												 Eliminar las vocales de una frase

#frase = input("Frase: ")
#vocales = 'aeiouAEIOU'						# esta variable es la que se usa para comparar con 'k', 											
#final = ''									# 55
#											#y se verifica si cuando 'k' toma el valor de un elemento de 'frase' es igual a algun elemento de 'vocales' (que es un objeto de caracteres)
#for k in frase:								
#											# en este ciclo se recorre con una variable cualquiera (en este caso 'k') todos los elementos del objeto frase (la frase que introducimos con el teclado)
#	if k not in vocales:					# se verifica si esa varible 'k' no es igual a ninguno de los valores de la varibale vocales
#		final+=k
#print(final)




													# Ejercicio 4
											# Pedir n palabras y colocarlase en un string separadas por un espacio

'''
n = int(input('Nro de palabras: '))
final=''

for i in range (n):
	pal = input()
	final+=pal+' '
print(final)
'''


														# Ejercicio 5
												# De dos conjuntos de caracteres realizar la interseccion (introducidos como un texto simple)

'''
def intersect(V, X):
	y=''
	for i in V:
		for k in X:
			if i==k:
				y += i
	return y

txt3=''
txt1 = input('Texto 1: ')
txt2 = input('Texto 2: ')
txt3 = intersect(txt1, txt2)
print('La interseccion (con elementos repetidos) es:',txt3)
'''

				
		
															# Ejercicio 6
													# Borra palabras


#'''
#def separacion(frase, separado):
#	cont=0
#	frase=frase+' '									#para evitar tener el problema de que no reconoce la ultima palabra por la falta del espacio, se añade un ' ' 
#	aux=''
#	for i in frase:
#		if i != ' ':
#			aux += i
#		else:
#			vec = aux
#			separado.append(vec)
#			aux=''
#			cont+=1
#	return cont

#def eliminacion(separado, palabra, n):
#	size=n
#	aux=0
#	for i in separado:
#		if i==palabra:
#			separado.pop(aux)
#			size-=1
#		aux+=1
#	print('\nEn forma de vector: ',separado,'\n')
#	print('En forma de texto: ', end='')
#	for k in range(size):
#		print(separado[k],'',end="")
	
#separado=[]
#frase = input('Frase: ')
#palabra = input('Palabra a borrar: ')
#n = separacion(frase,separado)
#eliminacion(separado, palabra, n)
#print('\n')
##'''


#																	 Ejercicio 6 (con funciones)
#																	Borra palabras


#frase=input('Frase: ')
#eliminar = input("Palabra a eliminar: ")
#final=frase.replace(eliminar, '')
#print(final)
													

															# Ejercicio 7
													# Funcion palindromo para ver si el string es palindromo y devolver True

'''
def EsPalindromo(pal_1, pal_2):
	if pal_1==pal_2:
		return print("True, es palindromo")
	else:
		return print("False, no es palindromo")

def volcar(pal_2):
	return pal_2[::-1]


pal_1=input("Palabra: ")
pal_2 = pal_1
pal_2 = volcar(pal_2)
EsPalindromo(pal_1, pal_2)
'''


														 #Ejercicio 8
										 #Unir dos listas de strings en una sola y ordenarlas alfabeticamente

A=[]
B=[]
print('Digite n para 1ra lista: ', end='')
n = int(input())
print('Digite m para 2da lista: ', end='')
m = int(input())

print('Nombres 1ra lista: ')
for i in range (n):
    vec = (input())
    A.append(vec)

print('Nombres 2da lista: ')
for i in range (m):
    vec = (input())
    B.append(vec)

A.extend(B)
A.sort()
print(A)
