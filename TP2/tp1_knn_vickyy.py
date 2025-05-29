import preprocessing as preproc
import math
import copy    					# Lo necesito para la segunda funcion

def file_to_matrix(filename):

	'''
	Recibe el nombre de un archivo .csv, lo abre y pasa los datos a una
	matriz por filas
	'''

	filename1=open(filename)    # Abro un archivo almacenado en la computadora.
	
	w0=filename1.readline()     # Leo la primera para eliminarla del output (no quiero el titulo).
	w1=filename1.readlines() 
	print(w1)						    # Empieza a leer desde la segunda linea. Se genera una lista de stings.
	i=0
	c=[]						# Creo una lista vacia para luego intoducir todas las observaciones.
	while i<len(w1):       
		l1=w1[i].split(",")     # Convierto CADA string de la lista en una lista de strings. 
							    # ["1,2,3","4,5,6"] EN ["1","2","3"] ["4","5","6"].
		j=0					   
		while j<len(l1):        
			l1[j]=float(l1[j])  # Cada string dentro de cada lista lo convierto en un float.
			         	        # ["1","2","3"] ["4","5","6"] EN [1,2,3] [4,5,6].
			j=j+1
		i=i+1
		c.append(l1)			# Agrego a la lista "c" con cada lista de floats (observaciones)
	
	print(c)
	filename1.close()			# Cierro el archivo. 
	return c 					# Devuelve una matriz.


	

def get_features(dataset): 
	
	'''
	- Recibe una matriz de datos por filas
	- Devuelve la matriz sin la primera columna (que sera la variable y)
	'''
	
	c=[]
	c=copy.deepcopy(dataset)    # por referencia crea una copia de la lista grande y las de adentro.
	for lines in c:
		del lines[0]
	print(c)
	return c

   

def get_y(dataset):

	'''
	- Recibe una matriz de datos por filas
	- Devuelve una lista con cada elemento de la primera columna (variable y)
	'''
	
	ms=[]						    # Genero una lista vacia.
	for lista in dataset:	      	# Recorro cada fila de la matriz (dataset).
		ms.append(lista[0])         # Agrego a la lista vacia el primer elemento de cada lista. 
	print(ms) 					
	return ms  				     	# Genero un vector de precios.

def euclidean_distance(x, y): 

	'''
	Recibe dos listas de igual cantidad de elementos y calcula la distancia.
	euclidea entre ellas
	'''
	
	i=0
	j=0
	suma=0
	c=[]
	nx=len(x)
	for i in range(nx):				# itero sobre el largo de la lista x.
		c.append((x[i]-y[i])**2)    # agrego a una lista la resta(al cuadrado) elemento a elemento de x e y.
		suma=suma+c[i]				# voy acumulando ese valor en una vble acumulativa.
	suma1=math.sqrt(suma)			# calculo la raiz de la suma final.
	
	return suma1


def get_distances(target, X, y_training):

	'''
	- Recibe una lista target, una lista de n listas (conjunto de features de
	  entrenamiento) y la lista de precios, también del conjunto de entrenamiento.
	- Devuelve una lista de n tuplas donde cada una contine, primero, la distancia
	  euclidea entre la i-esima observacion del conjunto de training y la observacion
	  target y, segundo, el precio asociado a la i-esima observacion de training.

	'''

	l=[]
	d=target
	i=0
	while i<len(X): 		 		     # len(X) nos dice cuantos departamentos hay.
		c=X[i] 						     # c es un departamento.
		dist = euclidean_distance(c,d)   # la distancia entre cada feauture (sin el precio).
		price= y_training[i]             # que precio le corresponde a ese departamento (c).
		pos=X.index(X[i])                # cual es el indice del departamento.
		t=(dist, price, pos) 		     # creo una tupla con cada resultado.
		l.append(t) 				     # a medida que se van generando las tuplas se van agregando a l. 
		i=i+1
	return l 						     # obtenemos una lista con tuplas de tamaño len(X)
									



def get_nearest_neighbors(distancias, k):
	'''
	- Recibe una lista de tuplas y un valor k de vecinos a considerar
	- Devuelve un lista con las k tuplas que tienen menor valor en la primera
	  posición de ellas (que representa una distancia euclidea)
	'''

	# Implementacion naive
	 

	dist_ordenada=sorted(distancias)    # Las tuplas se ordenan desde el primer elemento .

	return dist_ordenada[0:k]           # Me quedo conn las k tuplas más cercanas.
									    # Sigo teniendo una lista de tuplas solo que de tamaño k.


		

def predict(X_training, y_training, new_obs, k):
	'''
	- Calcula la distancia euclidea a todas las observaciones del
	conjunto de training
	- Se queda con las k de menor distancia
	- Promedia los valores de y en training de las observaciones mas
	cercanas
	'''
	# Obtiene una lista con la distancia a cada observacion de training set
	distancias = get_distances(new_obs, X_training, y_training) 

	# Se queda con las k observaciones mas cercanas
	k_vecinos = get_nearest_neighbors(distancias, k)

	
	# Exraemos los valores
	suma_precio = 0
	for tup in k_vecinos:                  # itero sobre cada tupla dentro de las mas cercanas.
		suma_precio = suma_precio + tup[1] # sumo el precio de cada tupla.
	promedio=suma_precio/len(k_vecinos)	   # promedio la suma de los precios.
	

	# Devolvemos el promedio de los valores.
	
	return promedio                        # Obtengo un float.


def knn(X_training, X_test, y_training, k):
	'''
	- Para cada elemento en el conjunto de test, predice el valor. 

	- Devuelve un lista de tantos elementos como filas haya en la matriz de test
	  con la prediccion del precio
	'''

	predicciones = []
	for i in range(len(X_test)):
		# Agrego a predicciones=[] cada promedio de precios sobre cada elemento de la base X_test.
		predicciones.append(predict(X_training, y_training, X_test[i], k))	

		
	# Mostramos mensaje de evolucion de la ejecucion.
		if (i+1) % 10 == 0:
			print('\tPredicted',(i+1),'out of',len(X_test),'observations')
		
			predicciones.append(predict(X_training, y_training, X_test[i], k))	

	print(predicciones)
	return predicciones

def write_predictions(preds, filename): 
	'''
	Escribe la lista preds (con las predicciones para cada registro del conjunto de test) en el archivo con nombre filename.
	La primera linea es el header (prediccion), luego una prediccion por linea.
	'''
	nombre_archivo=filename 
	file_new=open(nombre_archivo,"w") # Abro un archivo hablitandolo para escribir. 
	file_new.write("predicción \n")   # Escribo predicción y voy al siguiente renglon.
	for i in preds:					  # Para cada valor predecido:
		file_new.write(str(i))		  # 1) Lo convierto en un str asi lo puedo escribir.
		file_new.write("\n")		  # 2) Agrego un enter entre cada valor.
	file_new.close()				  # Cierro el archivo con todas mis modificaciones.

def main():

	# Parametros de ejecucion.
	# Base estandar
	#input_training = 'training.csv'
	#input_test = 'test.csv'
	#output_pred = 'prediction.csv'

	# Base small (para testear implementacion)
	input_training = 'training_small.csv'
	input_test = 'test_small.csv'
	output_pred = 'prediction_small.csv'

	# Cantidad de vecinos. Se puede variar.
	k = 3

	# Importamos datos de training y de testeo (sobre los que vamos a
	# querer predecir)
	print('Reading files....')
	training = file_to_matrix(input_training)
	X_test = file_to_matrix(input_test)

	print('Extracting features....')
	# Separamos features de la variable "y" a predecir
	X_training = get_features(training)
	y_training = get_y(training)

	# Estandarizamos los features. Para evitar data leakage, usamos la media
	# y la desviacion estandar solo de los datos de training
	print('Normalizing....')
	preproc.standarization(X_training, X_test)

	# Corremos el algoritmo de knn
	print('Predicting....')
	predicciones = knn(X_training, X_test, y_training, k)

	# Escribimos el archivo con las predicciones
	print('Writing predictions')
	write_predictions(predicciones, output_pred)

if __name__ == '__main__':
	main()

 