import numpy as np

def media(x):
	'''
	Calcula la media de la lista (de float) x.
	'''
	
	i=0
	sum=0
	while i<len(x):
		sum=sum+x[i]
		i=i+1
	c = round(sum/len(x),4)
	
	
	return c


	#c=np.mean(x)
	#print(c)
	#return c




def standarization(X_training, X_test):
	medias = []
	desvios = []

	# Calculamos medias y desvios
	for j in range(len(X_training[0])):
		column = [X_training[i][j] for i in range(len(X_training))]
		medias.append(media(column))
		desvios.append(np.std(column))

	column_standardization(X_training, medias, desvios)
	column_standardization(X_test, medias, desvios)

def column_standardization(dataset, medias, desvios):
	'''
	- Recibe una matriz de datos por filas, una lista de medias y otra de
	  desvios estandar
	- Opera sobre la matriz recibida por referencia, sustrayendo la media
	  y luego dividiendo por el desvio estandar columna a columna
	'''
	for i in range(len(dataset)):
		for j in range(len(dataset[0])):
			dataset[i][j] = (dataset[i][j] - medias[j])/desvios[j]

