import datetime
import unittest
from dateutil import tz
import urllib.request
import json
import sys
import matplotlib.pyplot as plt
plt.style.use("dark_background")
import requests

############################# FUNCIONES AUXILIARES DEFINIDAS POR EL GRUPO ############################### 

def get_quote_json(q, init_date, end_date, interval):

    '''Accede a la API de Yahoo! Finance para la accion "q", con la fecha de inciio, fin, e intervalo 
    correspondiente y devuelve el JSON (dict) correspondiente.'''

    url="https://query2.finance.yahoo.com/v8/finance/chart/"+str(q)     
    try:
        params={
            "period1":str(init_date),
            "period2":str(end_date),
            "interval":str(interval)

            }

        req=requests.get(url,params=params)                     
        req_json=req.json() 
        return req_json

    except Exception as e:
        print(e)


def rendimientos_diarios(l):
    rendimiento=[]
    j=1
    while j<len(l):
        rendimiento.append((l[j]/l[j-1])-1)
        j=j+1
    return rendimiento
        

def rendimientos_posibles(l): # los elementos dentro de l son mayor estricto a 0.
    rendimientos_obtenibles=[]
    for i in range(len(l)): 
        for j in range(i+1, len(l)): # itero sobre todos los elementos siguientes sin repetición.
                rendimiento1=(l[j]/l[i])-1              
                rendimientos_obtenibles.append(rendimiento1)
    s=max(rendimientos_obtenibles)
    # print(len(rendimientos_obtenibles))
    # print("Rendimientos obtenibles:",rendimientos_obtenibles)
    return s

def max_rend_aux(l1,l2):
    for k in range(len(l1)):
            for f in range(k+1,len(l1)):
                 # comparo para encontrar la posicion
                if ((l1[f]/l1[k])-1)>=rendimientos_posibles(l1):
                    dias_transcurridos=f-k  
                    t=[to_ymd(l2[k]), to_ymd(l2[f])]               
                    print("compra:",to_ymd(l2[k]),"venta:",to_ymd(l2[f]))
                    print("dias_transcurridos",dias_transcurridos) 
    return t 

def aplicacion_ej6():
    w=["2019-12-10", "2021-05-10", "1mo", "MELI", "ZM", "AAL"] #parametros que usaremos 
    aplicacion=open("aplicacion.cfg", "w") 
    i=0 
    n=len(w)-1
    while i<n: 
        aplicacion.write(str(w[i])+ "\n")
        i=i+1
    aplicacion.write(str(w[n]))
    aplicacion.close() 
    s=open("aplicacion.cfg") 
    archivo=s.read() 
    archivos2=archivo.split("\n")
    return archivos2

 
############################# FUNCIONES AUXILIARES DEFINIDAS POR LA CATEDRA ############################### 
def to_date(strdate):
    '''toma un string en formato %Y-%m-%d y lo convierte a algo de tipo fecha'''
    return datetime.datetime.strptime(strdate, '%Y-%m-%d')

def to_ymd(ts):
    ''' Toma un timestamp y lo convierte a un string con formato %Y-%m-%d'''
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

def to_posix_timestamp(date):
    '''Toma un datetime y lo convierte a timestamp formato POSIX'''
    return (date - datetime.datetime.utcfromtimestamp(0)).total_seconds() + 14400

# TEST UNITARIO (para correr el test hay que des esto)



############################# FUNCION PRINCIPAL ############################### 
def main():
    ''' Es la funcion principal donde se ejecuta nuestro programa.'''

    # EJERCICIO 1: Leemos el archivo input.cfg con los parametros para la ejecucion.
    

    file=open("input.cfg")
    files=file.read()
    files2=files.split("\n")
    print(files2)
    file.close()

    # Defino las variables que voy a usar en mi funcion get_quote_json en formato timestamp
    init_date=round(to_posix_timestamp(to_date(files2[0]))) 
    end_date=round(to_posix_timestamp(to_date(files2[1])))

    # print(init_date) 
    # print(to_ymd(init_date)) cheuqeo si el timestamp estaba bien 
    # print(end_date)
    # print(to_ymd(end_date))

    # Genero una lista con todas las acciones a analizar 
    acciones=[] 
    for i in files2[3:]:
        acciones.append(i)
    
    rendimientos=[]     # Esta lista la genero para los graficos 

    for i in acciones:  # Voy recorriendo cada accion 

    #EJERCICIO 2
        json=get_quote_json(i,init_date,end_date,files2[2])

    #EJERCICIO 3
        # Calculo los precios 
        i_fechas=json["chart"]["result"][0]["timestamp"]
        print(str(i)+"_fechas:", i_fechas)

        i_precios=json["chart"]["result"][0]["indicators"]["adjclose"][0]["adjclose"]
        print(str(i)+"_precios:",i_precios)

        i_rendimiento=rendimientos_diarios(i_precios)
        print("rendimientos_diarios_"+str(i)+":",i_rendimiento)
        rendimientos.append(i_rendimiento)
        
    # EJERCICIO 5 

        # Busco el maximo rendimiento posible 
        i_max_rend=rendimientos_posibles(i_precios)
        print("Max_rend_posible_"+str(i)+":",i_max_rend)
        # Busco en que fecha ocurriria:
        max_rend_aux(i_precios,i_fechas)
       
        # Genero una lista con las fechas (son las mismas para todas las acciones)
        fechas=[]
        for j in range(len(i_fechas)):
            fechas.append(to_ymd(i_fechas[j]))
        print("fechas:", fechas)
    

    # EJERCICIO 4

    x=list(fechas[1:])
    y=[0]*len(x)
    z=[0]*len(x)
    k=[0]*len(x)
    
  
    for j in range(len(x)):
        y[j]=rendimientos[0][j]
        z[j]=rendimientos[1][j]
        k[j]=rendimientos[2][j]

    plt.plot(x,y,"r-o")
    plt.plot(x,z,"b-o")
    plt.plot(x,k,"g-o")
    plt.legend(["rendimientos_AMZN","rendimeintos_TSLA","rendimeintos_FDX"])
    plt.show()

    # EJERCICIO 6
    
    # Vamos a repetir el procedimiento de los puntos anteriores con otras fechas y acciones.

    fecha_inicial=round(to_posix_timestamp(to_date(aplicacion_ej6()[0]))) 
    fecha_final=round(to_posix_timestamp(to_date(aplicacion_ej6()[1])))

    # Generamos una lista con las nuevas acciones
    acciones_aplicacion=[] 
    for elem in aplicacion_ej6()[3:]:
        acciones_aplicacion.append(elem)
        print(acciones_aplicacion)

    
    rendimientos_aplicacion=[] # SERVIRÁ A LA HORA DE GRAFICAR
    precios_aplicacion=[]      # SERVIRÁ A LA HORA DE GRAFICAR

    for a in acciones_aplicacion:

        json_ap=get_quote_json(a,fecha_inicial,fecha_final,aplicacion_ej6()[2]) #en el termino archivos2[2] aparece la granuralidad de los datos
        a_fechas=json_ap["chart"]["result"][0]["timestamp"] 
        print(str(a)+"_fechas:", a_fechas)

        a_precios=json_ap["chart"]["result"][0]["indicators"]["adjclose"][0]["adjclose"]
        print(str(a)+"_precios:",a_precios)
        precios_aplicacion.append(a_precios)
        
        a_rendimiento=rendimientos_diarios(a_precios)
        print("rendimientos_diarios_"+str(a)+":",a_rendimiento)
        rendimientos_aplicacion.append(a_rendimiento)
        
        fechas_aplicacion=[]
        for j in range(len(a_fechas)):
            fechas_aplicacion.append(to_ymd(a_fechas[j]))
        print("fechas:", fechas_aplicacion)

        
    #Graficamos evolucion de los precios

    x=list(fechas_aplicacion[1:])
    y=[0]*len(x)
    z=[0]*len(x)
    k=[0]*len(x)

    for j in range(len(x)):
        y[j]=precios_aplicacion[0][j]
        z[j]=precios_aplicacion[1][j]
        k[j]=precios_aplicacion[2][j] 

    plt.semilogy(x,y,"r-o")
    plt.semilogy(x,z,"b-o")
    plt.semilogy(x,k,"g-o")
    plt.legend(["precio_accion_MERCADO_LIBRE","precio_accion_ZOOM","precio_accion_AMERICAN_AIRLINES"])
    plt.show() 

    


if __name__ == '__main__':
    main()