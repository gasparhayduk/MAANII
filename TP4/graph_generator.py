# coding: utf-8 
import pickle
from bs4 import BeautifulSoup
import networkx as nx
import sys
import matplotlib.pyplot as plt

######################## FUNCIONES PARA COMPLETAR ########################
def get_posts(html):
	'''Dado un html bajado con el scrapper, extrae los posts del mismo y los devuelve en una lista. 
	Los posts son instancias de clases de BeautifulSoup'''

	soup=BeautifulSoup(html,"lxml") 
	postbody=soup.find_all(class_='postbody')
	posts=[]

	for post in postbody:
		#print(post)
		posts.append(post)

	return posts 

def get_post_user(post):
	'''Dado un post, extrae el usuario autor del post.'''
	author=post.find(class_='author')
	splan=author.find(class_='responsive-hide')
	a=splan.find('a')
	if a!=None:
		post_user=a.get_text()

		return post_user 

def get_post_cites(post):
	'''Dado un post, extrae los usuarios citados por el autor del post. Devuelve una lista, ya que un post puede tener multiples citas.'''
	
	citados=[]
	contenido = post.find("div", class_="content")
	blockquote=contenido.find_all('blockquote')

	if blockquote != None:
		for elem in blockquote:
			cite=elem.find('cite')
			if cite!=None:
				user_citado=cite.find('a')
				if user_citado != None:
					user_citado=user_citado.get_text()
					citados.append(user_citado) 

	return citados
	
# Agregar aca las funciones que consideren necesarias.



def posts_realizados(usuario, FORO): #agarra un usuario y una lista de tuplas con usuario y citados para todos los posteos del foro y calcula cuantos posteos realizo usuario
	#con esta funcion, sabremos que usuarios son los que hacen mas posteos.
	cant_posteos=0
	for post in FORO:
		if post[0]==usuario:
			cant_posteos=cant_posteos + 1

	return cant_posteos


def interacciones(tupla, FORO): #recibe como parametro una tupla (o bien, un edge: un par (user,citado)) y un foro (usuario y citados por posteo), y retorna cuantas veces interactuaron entre sí dentro del FORO 
	cant_interacciones = 0
	for elem in FORO: #accedemos para cada posteo
		if elem[1]!=[]: #caso en que haya citados
			for citado in elem[1]: #accedemos para todos los citados dentro de un post
				if tupla==(elem[0], citado) or  tupla==(citado, elem[0]):         #elem [0] es un autor del post       
					cant_interacciones = cant_interacciones + 1
	return cant_interacciones 

######################## MAIN ########################

def main():
	'''En este modulo vamos a tomar la informacion bajada de manera masiva y generar nuestro 
	modelo de la red de interaccion en el foro.'''
	#temas = [("ALUA", "http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=48"), ("TSLA", "http://foro.rava.com/foro3/viewtopic.php?f=7&t=265") , ("COME", "http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=70"), ("Dow_Jones", "http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=52")]
	temas=["ALUA", "TSLA", "Dow_Jones", "COME"]

	# Definir el grafo a considerar (dirigido, no dirigido, con pesos, sin pesos, etc). 
	#Haremos un grafo dirigido por tema, e interaremos ver cuales son los usuarios que mas interactuan entre sí y ver que usuarios son los que hacen mas posteos dentro de cada tema.
	# Esto es eleccion de cada grupo.

	for tema in temas:
		# Arbir el archivo del tema. Por requerimiento de pickle, tiene que ser abierto como lecutra y binario. 
		# La forma de hacer esto es segundo parametro 'rb'.
		with open(tema + ".p",'rb') as f:
			htmls_tema=pickle.load(f) #htmls es una lista donde en cada elemento esta el html de una pagina

		FORO_tema=[] #creamos una lista vacia donde appendearemos las tuplas con los usuarios del post y las citas en caso de haber

		for html in htmls_tema: #para cada pagina
			posts_tema=get_posts(str(html)) #obtenemos una lista donde esten los posteos de una pagina
			for post in posts_tema: #para cada posteo obtenemos quien lo hizo y a quienes citó
				user=get_post_user(post)
				cites=get_post_cites(post)
				t=(user, cites)
				FORO_tema.append(t) #en FORO tenemos una lista donde cada elemento está el user y las citas de un posteo, y asi para todos los posteos dentro de las 300 paginas analizadas. Acá está toda la informació importante.

		usuarios_tema=[] #crearemos una lista con todos los usuarios que participan en el foro

		for elem in FORO_tema: #accedemos para todos los posteos
			if elem[0] not in usuarios_tema: #elem[0] es el autor del posteo, hacemos esto para no repetir usuarios. Al decir 'if elem[0] not in usuarios' estamos diciendo que appende en caso de que el usuario todavia no esté en la lista de usuarios. 
				usuarios_tema.append(elem[0])
			#tambien debemos considerar el caso en el que un usuario sea citado en el foro pero que no haya posteado nada. Para ello, inspeccionamos el segundo elemento de cada tupla
			for w in elem[1]: #accedemos para todos los citados dentro de un post
				if w not in usuarios_tema and elem[1]!=[]:
					usuarios_tema.append(w)

		#en usuarios tenemos los nodos del grafo, faltan los ejes.

		#definimos el digrafo:
		G_tema=nx.DiGraph()

		#definimos los nodos:
		for usuario in usuarios_tema:
			G_tema.add_node(usuario, posteos_realizados=posts_realizados(usuario, FORO_tema)) #creamos los nodos, cada nodo tendrá como atributo la cantidad de posteos que dicho nodo (usuario) hizo


		#definimos los edges:
		for elem in FORO_tema: #accedemos para todos los postoes
			if elem[1] !=[]: #solo construimos ejes para los casos en que un usuario cite a otros, por eso elem[1]  no debe ser una lista vacia.
				for a in elem[1]: #accedemos para todos los citados
					G_tema.add_edge(elem[0], a, weight=interacciones((elem[0], a), FORO_tema))

		nx.write_gml(G_tema, tema + ".gml")

if __name__ == "__main__":
	main()
