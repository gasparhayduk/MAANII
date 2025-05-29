def minimo(x,y):
	if x <= y: #si X es menor a Y, el minimo es X
		minimo=x
	else: #aca estamos en el caso donde X es mayor que Y, por lo que Y es el minimo entre esos dos numeros
		minimo=y
	return minimo	
	#print(minimo)

	

			


def minimo_3(x,y,z): #la idea es comparar los tres numeros de a pares. Comparo X con Y, comparo X con Z, comparo Z con Y, y de esas comparaciones, me quedo con el menor
	par1=minimo(x,y) #aca comparamos  X con Y, y definimos a par1 como el minimo entre X e Y 
	par2=minimo(x,z) #aca comparamos  X con Z, y definimos a par2 como el minimo entre X e Z
	par3=minimo(y,z) #aca comparamos  Y con Z, y definimos a par3 como el minimo entre Y e Z

	if par1 <= par2 and par1 <= par3: #para que par1 sea el minimo, debe ser menor a par2 y par3
		minimo_3numeros = par1
	if par2 <= par1 and par2 <= par3: #para que par2 sea el minimo, debe ser menor a par1 y par3
		minimo_3numeros = par2
	if par3 <= par1 and par3 <= par2: #para que par3 sea el minimo, debe ser menor a par1 y par2
		minimo_3numeros = par3	

	return minimo_3numeros

	#print(minimo_3numeros)		
	

def contar_pares(l): #tenemos una lista, debemos pasar sobre todos sus elementos (usaré while), ver si un elemento es par, y contar todos los pares
	n=len(l) #con esto, sabemos cuantos elementos tiene la lista
	i=0 #con i, nos referimos al elemento en la posicion i. Empezamos en i=0 pues asi hacemos referencia a la primera posicion
	cant_pares=0 #con 'cant_pares', contamos la cantidad de pares. Empieza valiendo 0 
	#ahora, creo un codigo que me permite moverme de la posicion 0 hasta la posicion n-1. While sirve para hacerlo

	while i < n: #iteramos desde i hasta n
		D=l[i] / 2 #hacemos la division entre i y 2
		D_1=l[i] // 2 #hacemos la division entera entre e i y 2

		if D == D_1: #si la division entera entre i y 2 es igual a la division entre i y 2, entonces i es par
			cant_pares=cant_pares + 1 #actualizamos la cantidad de pares en caso de que el elemento de la posicion i lo sea
		
		i=i+1 #nos movemos a la siguiente posicion 

	return cant_pares
	#print(cant_pares)	

def posicion_minimo_lista(l):
	n=len(l) #con esto, sabemos cuantos elementos tiene la lista
	i=0 #empezamos en la primera posicion
	minimo_lista=l[0]	#esta variable guardara que elemento es el minimo, empezamos desde 0
	while i+1<n: #empezamos a iterar desde la posicion i+1 hasta la posicion n, pues dijimos que el minimo esta la posicion i (0 al empezar)
		if l[i+1]<=minimo_lista: 
			minimo_lista=l[i+1] #si el elemento de la posicion i+1 es menor al minimo de la lista, entonces el elemento de la posicion i+1 pasará a ser el minimo de la lista
		i=i+1 #nos movemos hacia la siguiente posicion
	#con el bloque anterior, sabemos cuál es el elemento minimo, ahora debemos ver en qué posicion está dicho elemente	
	i=0 #a la variable i (que usamos anteriormente), le damos el valor 0 para iterar desde la posicion 0 hasta la n y ver si el elemente minimo está en esa posicion
	while i<n: 
		if l[i]==minimo_lista:
			pos=i #si el elemento de la posicion i es el minimo de la lista, entonces en la posicion i está el minimo. La variable 'pos' guardará en qué posició está el elemento minimo de la lista.
		i=i+1 #nos movemos a la siguiente posicion			
	return pos #nos devuelve cual es la posicion donde está el elemento minimo de la lista  




def media(l):
	n=len(l) #sabemos la cantidad de elementes aue tiene
	i=0 #empezamos en esta posicion
	suma_elementos=0 #esta variable acumulara la suma de los elementos. Como es acumulativa, la hacemos empezar en 0

	while i<n:
		suma_elementos= suma_elementos + l[i] #con esto, vamos acumulando la suma de los elementes
		i=i+1 #nos movemos a la siguiente posicion

	media=suma_elementos/n #la media es la suma de los elementos dividido la cantidad de elementes. 
	return media
	#print(media)	

def reverso(l): 
	n=len(l) #con esto, sabemos cuantos elementos tiene l
	i=0 #empezamos en la primera posicion
	l1=l.copy() #creamos una lista l1 que sea una copia de l, sobre la cual daremos vuelta la lista l 
	while i<n: #iteramos desde la primera posicion hasta la ultima
		l1[i]=l[n-1-i] #aca, al empezar en la posicion i=0, cambiamos el elemento de la posicion 0 por el elemento de la utlima posicion, y hacemos eso con todas las posiciones
		i=i+1 #nos movemos a la siguiente posicion
	return l1
	

#otra alternativa que se me ocurrió pero que no sirve para el ejercicio de capicua es la siguiente:

#def reverso(l):
#	n=len(l) #con esto, sabemos cuantos elementos tiene l
#	w=[] #creamos una lista vacia donde insertaremos los elementos de i en posicion inversa
#	i=0 #empezamos en la primera posicion
#	while i<n: #iteramos desde i=0 hasta n 
#		w.insert(i,l[n-1-i]) #insertamos en la lista vacia 'w' los elementos de l al reves. Por ejemplo, para i=0, insertamos en la primera posicion de 'w' el ultimo elemento de l 
#		i=i+1 #pasamos a la siguiente posicion 
#	return w	





def es_capicua(l):
	l_prima=reverso(l) #dada una lista l, la lista l_prima es l pero con los elementos al reves, por eso aplicamos reverse
	if l==l_prima: #si l y l_prima son iguales, es xq l es capicua
		ret = True
	else: #si l y l_prima no son iguales, es xq l no es capicua
		ret = False
	return ret	
	#print(ret)		



def concatenar(l1,l2): 
	n=len(l2) # notar que pusimos l2 pues vamos a iterar sobre l2
	i=0 # primera posicion
	l3=l1.copy() #creamos una lista l3 que sea una copia de l1, sobre la cual concatenaremos los valores de l2

	while i<n:
		l3.append(l2[i]) # a l3 (recordae que l3 es una copia de l1), le anexamos en la ultima posicion el elemento de la posicion i de l2
		i=i+1 # nos movemos a la siguiente posicion
	return l3	
	#print(l3)	


def sumar_listas(l1,l2):
	n=len(l1) #con esto, sabemos cuantos elementes tienen l1 y l2 (ambas tienen la misma cantidad de elementos, supuesto del ejercicio)
	i=0 #empezamos de la posicion 0
	w=[] #creamos una lista vacia sobre la cual vamos a insertar la suma de los elemenros de l1 y l2

	while i<n: #iteramos desde i hasta n, para pasar por toda la lista
		suma=l1[i]+l2[i] #definimos la variable 'suma' como la suma del elemento de la posicion i de la lista l1 y el elemento de la posicion i de la lista l2
		w.insert(i,suma) #en la lista vacia 'w', inseramos en la posicion i la suma de los elementos de l1 y l2 de la posicion i
		suma=0 #antes de pasar a la siguiente posicion, limpiamos 'suma' así no sumamos elementos de diferentes posiciones
		i=i+1 #nos movemos a la segunda posicion  
	return w

		

def quitar_apariciones(l,elem):
	n=len(l)
	i=0
	elem=elem
	while i<n:
		if l[i]==elem: #si cuando iteramos y el elemento de la posicion i es igual a elem (el parametro de la funcion), debemos eliminar dicho elemento y hacer algunos cambios en i y n
			del l[i] #es importante notar que cuando eliminamos un elemento, la longitud de la lista cambia, por eso debemos actualizar algunos valores
			n=len(l) #actualizamos el valor de n en caso de eliminar un elemento
			i=i-1 #con esto, compensamos la posicion en caso de eliminar un elemento para iterar
		i=i+1	#avanzamos en la siguiente posicion
			
	return l #notar que todos los cambios se hicieron sobre la lista original l, y no en una copia

def calcular_elemento_minimo(l): #ESTA ES UNA FUNCION AUXILIAR PARA RESOLVER EL EJERCICIO DE ORDENAR_LISTA(l), esta funcion nos devuelve cual es el elemento minimo de una lista l
	n=len(l) #con esto, sabemos cuantos elementos tiene la lista
	i=0 #empezamos en la primera posicion
	minimo_lista=l[0]	#esta variable guardara que elemento es el minimo, empezamos desde 0
	while i+1<n: #empezamos a iterar desde la posicion i+1 hasta la posicion n, pues dijimos que el minimo esta la posicion i (0 al empezar)
		if l[i+1]<=minimo_lista: 
			minimo_lista=l[i+1] #si el elemento de la posicion i+1 es menor al minimo de la lista, entonces el elemento de la posicion i+1 pasará a ser el minimo de la lista
		i=i+1 #pasamos a la siguiente posicion 

	return minimo_lista #nos devuelve cual es el elemento minimo de una lista l

def ordenar_lista(l): 
	n=len(l) #sabemos cuantos elementos tiene 'l'
	z=l.copy() #creamos una lista 'z' que sea una copia de 'l'
	w=[] #definimos una lista vacia 'w' donde iremos almacenando los elementos de l en forma ascendente
	i=0 #empezamos en la primera posicion	

	while i<n: #iteramos desde i=0 hasta n
		minimo_lista=calcular_elemento_minimo(z) #calculamos cual es el elemento minimo de z (recordar que z es una copia de l) usando la funcion auxiliar calcular_elemento_minimo
		pos=posicion_minimo_lista(z) #usando la funcion posicion_minimo_lista definida en el ejercicio 3, podemos saber en qué posicion se encuentra el elemento minimo de una lista
		w.append(minimo_lista) #a la lista vacia 'w', le agregamos el elemento minimo de z
		del z[pos] #eliminamos el elemento minimo de la lista z, asi en la siguiente iteracion la funcion auxiliar calcular_elemento_minimo calculará el segundo elemento minimo de l
		i=i+1 #pasamos a la siguiente posicion 
	return w 
	#notar que en ningun momento modificamos a l	

			


	

	
def fibo_recursiva(n):
	if n==0: #caso basico n=0
		ret=0
	elif n==1: #caso basico n=1
		ret=1
	else: #n!=0 y n!=1
		ret=fibo_recursiva(n-1) + fibo_recursiva(n-2)
	return ret	

		

def primos_hasta(n):
	w=[]	#creamos una lista vacia donde iremos agregando los numeros primos entre 0 y n
	i=2     #esta es la variable donde iteraremos, la empezamos en 2 xq ni 0 ni 1 son primos
	
	if n==0:
		print(w) #si nos piden los numeros primos entre 0 y 0, la listab sera vacia pues 0 no es primo
	elif n==1: 
		print(w)	#si nos piden los numeros primos entre 0 y 1, la lista estara vacia pues 1 no es primo
	else: #aca estamos en el caso donde n es mayor a 1
		while i<=n: #iteramos desde 2 hasta n
			divisor=2 #la variable 'divisor' sera la variable por la cual dividiremos a i, e ira desde 2 hasta i-1.Por ejemplo, si tenemos i=4, dividiremos a 4 entre 2 y 3. Eso hara la variable 'divisor'
			es_primo=True #empezamos asumiendo que un numero es primo hasta que pase la prueba
			 
			while es_primo==True and divisor<i: #esta es la prueba para ver si i es primo
				if i % divisor==0: #si la division entera entre i y divisor es 0, i no es primo
					es_primo=False
				else:
					divisor=divisor+1 #hacemos que divisor avance un numero. Por ejemplo, si tenemos 3 y primero lo dividimos por 2, la primera condicion no se cumpliara y debemos pasar a dividir por 3
			if es_primo==True: #si supera la prueba, es primo y entonces a la lista vacia 'w' le agregamos un elemento
				w.append(i)                         
			i=i+1 #avanzamos ak siguiente numero
	return w	

			

def main():
	#x= 0
	#y= 0
	#z= 0
	#minimo_3(x,y,z) #ejecutamos la funcion minimo(x,y,z)
	
	

	# En el main les proveemos algunas pruebas basicas para las funciones del TP
	# Estan originalmente comentadas para que puedan ejecutar el codigo de forma gradual.
	# La sugerencia respecto a la ejecucion es la siguiente.
	# 1. Decidir la funcion a implementar (ejemplo: minimo).
	# 2. Implementarla.
	# 3. Venir al main, y buscar los casos de test correspondietes.
	# 4. Descomentar las lineas correspondientes y probar la ejecucion.
	# 5. En caso de encontrar errores, tratar de corregirlos hasta que la implementacion sea correcta.
	#6. Opcionalmente, agregar casos de prueba que consideren necesarios.
	# 7. Pasar a la siguiente funcion.
	
	#a = 1
	#b = 10
	#c = 20
	#l1 = [1,2,3]
	#contar_pares(l1)
	#l2 = [4,5,6]
	#print(media(l2))
	#l3 = ['a','b','b','a']
	#l4 = [6,2,3,16,9,3,13,4,1]
	#elem = 5
	#n = 10 

	# test minimo.
	# descomentar las siguientes dos lineas
	 print('minimo: ', minimo(a,b))
	# print('minimo: ', minimo_3(a,b,c))

	# test contar_pares
	# descomentar las siguientes dos lineas
	# print('contar_pares: ', contar_pares(l1))
	# print('contar_pares: ', contar_pares(l2))
	
	#test posicion_minimo_lista
	# descomentar las siguientes dos lineas
	 #print('min_lista: ', posicion_minimo_lista(l1))
	 #print('min_lista: ', posicion_minimo_lista(l2)) 

	# test media
	# descomentar las siguientes dos lineas
	# print('media: ', media(l1))
	# print('media: ', media(l2))

	# test reverso
	# descomentar las siguientes dos lineas
	# print('reverso(l1): ', reverso(l1))
	# print('reverso(l3): ', reverso(l3))

	# test es_capicua
	# descomentar las siguientes tres lineas
	# print('es_capicua(l1): ', es_capicua(l1))
	# print('es_capicua(l2): ', es_capicua(l2))
	# print('es_capicua(l3): ', es_capicua(l3))

	# test concatenar
	# print('concatenar: ', concatenar(l1,l2))

	# test sumar_listas
	# descomentar la siguiente linea
	# print('sumar_listas: ', sumar_listas(l1,l2))

	# test quitar_apariciones
	# descomentar las siguientes dos lineas
	# quitar_apariciones(l3,'b')
	# print('sin aparciones: ', l3)

	# test ordenar_lista
	# descomentar la linea que sigue
	# print('ordenar_lista: ', ordenar_lista(l4))

	# test fibonacci
	# descomentar las siguientes dos lineas
	# print('fibo rec: ', fibo_recursiva(n))

	# test primo_hasta
	# descomentar las siguientes lineas
	# print('primo_hasta', primos_hasta(n))


if __name__ == '__main__':
	main()
