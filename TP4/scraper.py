# coding: utf-8

import pickle

from bs4 import BeautifulSoup

import urllib.request

from random import random

from time import sleep

import sys



######################## FUNCIONES PARA COMPLETAR ########################

def link_siguiente(html):

    """ Función que toma con input código html de una página del foro de rava online

    ya parseado con bs4 y devuelve el link que figura en el botón de siguiente. De

    no estar este botón activo, debe devolver None. """


    pagination=html.find(class_='pagination')

    next_=pagination.find(class_='next')


    if next_==None:

        return None

    else:

        a=next_.find('a')
        a1=a["href"][1:]
        link="http://foro.rava.com/foro3"+a1

        # print(link)


    return link 



def scrapear_tema(url, max_pages = 10):

    """ Funcion que toma el link inicial de tema del foro de rava online y baja el html

    del mismo. Debe devolver una lista en donde cada elemento es codigo html de una pagina.

    (IMPORTANTE: guardado como unicode)"""


    i=0

    htmls=[]



    while i<300:

            # Hack: esta linea evita algunos errores en las respuestas. Dejarla.

            sleep(0.35 + random()) 

            # Para bajar la pagina, pueden usar urllib.request.urlopen y pasarle la direccion de la pagina.

            page_html = urllib.request.urlopen(url).read().decode("utf-8") #obtiene el html de la primera pagina

            htmls.append(page_html)

            # Setear el formato en el que se interpretan los caracteres.

            soup = BeautifulSoup(page_html, "lxml") #lmxl es el formato, usaremos esto. En soup tenemos un objeto con el que podremos interactuar con el html

            #Guardamos el contenido de la pagina:

            # Obtener el link siguiente.

            url=link_siguiente(soup)

            if url==None:
                break
        
            i=i+1

    return htmls

######################## MAIN ########################

def main(): 



    # Ejemplo con listado de temes. Pueden modificarlo agregando/sacando temas.

    temas = [("ALUA", "http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=48"),

             ("TSLA", "http://foro.rava.com/foro3/viewtopic.php?f=7&t=265"),

             ("COME", "http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=70"),

             ("Dow_Jones", "http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=52")]



    #print(scrapear_tema("http://foro.ravaonline.com/foro3/viewtopic.php?f=1&t=48"))

    # Este es el loop principal del scraper


    for tema, url in temas:

        # Obtener los htmls del tema.

        html = scrapear_tema(url)
        
        # Guardar la lista usando pickle. Observacion: por requerimiento del modulo pickle el archivo tiene que ser abierto como lectura y binario.

        file = open(tema + ".p",'wb')

        pickle.dump(html, file)

        file.close()


        # Esto se especifica utilizando como parametro 'wb', que sigifnica 'write' y 'binary'.



    

if __name__== "__main__":

    main()

