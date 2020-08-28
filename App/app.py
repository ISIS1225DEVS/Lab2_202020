"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
import Support as sup
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from time import process_time
from Sorting import insertionsort

#Funciones programa

def loadCSVFile (file, lst,Type='SINGLE_LINKED',sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList(Type) #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst    

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    iterator=it.newIterator(lst)
    meter=0
    while it.hasNext(iterator):
        movie=it.newIterator(lst)
        if movie[column] == criteria:
            meter+=1
    return meter

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    return 0

def SearchbyDirector(lst,lst2,name_director):
    """
    retorna: La lista de todas las películas dirigidas, El numero de las películas y El promedio de la calificación de sus películas.
    """
    avgsum= 0
    info_movies=sup.findmoviesDirector(name_director, lst)
    size=len(info_movies)
    list_movies=[]
    iterator2=it.newIterator(lst2)
    while it.newIterator(iterator2):
        movie=it.next(iterator2)
        i=0
        found=False
        while i < size and not found:
            if movie['id'] == info_movies[i]['id']:
                list_movies.append(movie['title'])
                avgsum+= movie["vote_average"]
                found=True
            i+=1
    avg=avgsum/size
    return(list_movies,size,avg)

def SearchbyActor(lst,lst2,name_actor):
    """
    retorna: La lista de todas las películas en que participó. El numero de las películas. El promedio de la calificación de sus películas. El nombre del director con mas colaboraciones.
    """
    avgsum= 0
    info_peliculas=[]
    lista_peliculas=[]
    dict_directores={}
    iterador= it.newIterator(lst)
    while it.hasNext(iterador):
        movie= it.next(iterador)
        if movie['actor1_name'].lower() or movie['actor2_name'].lower() or movie['actor3_name'].lower() or movie['actor4_name'].lower() or movie['actor5_name'].lower() == name_director.lower():
            info_peliculas.append
            name_director= movie["director_name"]
            if name_director in dict_directores.keys():
                dict_directores[name_director]+=1
            else:
                dict_directores[name_director]=1

    iterador2=it.newIterator(lst2)
    while it.newIterator(iterador2):
        movie=it.next(iterador2)
        i=0
        found= False
        while i < len(lista_peliculas) and not found:
            if movie['id'] == info_peliculas[i]['id']:
                lista_peliculas.append(movie['title'])
                avgsum+= movie["vote_average"]
            i+=1
    director= max(dict_directores)
    avg=avgsum/len(info_peliculas)
    return(lista_peliculas,len(info_peliculas),avg,director)

def meetGenre(lst, lst2, genre):
    """
    Retorna:
        -lista con la informacion de las peliculas, el numero de peliculas y la votacion promedio. 
    """
    avgsum=0
    info_movies=sup.findmoviesGenre(genre, lst2)
    list_movies=[]
    size=len(info_movies)
    i=0
    while i < size:
        list_movies.append(info_movies[i]['title'])
        avgsum+=info_movies[i]['vote_count']
        i+=1
    avgsum=avgsum/size
    return(list_movies, size, avgsum)

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList('ARRAYLIST')   # se require usar lista definida
    lista2 = lt.newList('ARRAYLIST')
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                print("\n seleccione 1 para cargar la lista 1 o 2 para cargar la lista 2")
                lista_cargar=input('Seleccione la lista a cargar:\n')
                if lista_cargar == "1":
                    lista=loadCSVFile("Data\MoviesCastingRaw-small.csv",lista)
                    print("Datos cargados, ",lista['size']," elementos cargados")
                elif lista_cargar == '2':
                    lista2=loadCSVFile("Data\SmallMoviesDetailsCleaned.csv",lista2)
                    print("Datos cargados, ",lista2['size']," elementos cargados")
                else:
                    print('selecione una opcion valida')
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()