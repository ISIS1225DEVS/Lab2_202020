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
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as ls

from time import process_time 


def loadCSVFile (file, cmpfunction):
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=";"
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
#Comparación de datos

def compareRecordIds (element1, element2):
    if int(element1["id"]) == int(element2["id"]):
        return 0
    elif int(element1["id"]) > int(element2["id"]):
        return 1
    return -1

#Ordenamiento de datos

def topMovies(element1, element2):
    if (int(element1['vote_count']) > int(element2['vote_count'])):
        return True
    return False

def lowMovies(element1, element2):
    if (int(element1['vote_count']) < int(element2['vote_count'])):
        return True
    return False

def topMoviesAve(element1, element2):
    if (float(element1['vote_average']) > float(element2['vote_average'])):
        return True
    return False

def lowMoviesAve(element1, element2):
    if (float(element1['vote_average']) < float(element2['vote_average'])):
        return True
    return False



# Cargador de Datos

def loadMovies():
    lst = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting():
    lst = loadCSVFile("Data/MoviesCastingRaw-small.csv", compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

#Consola
def printMenu():
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Ranking de películas")
    print("4- Conocer el trabajo de un director")
    print("0- Salir")
#Función de cantidad de datos

def countElementsFilteredByColumn(criteria, column, lst):
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

# Función requerimiento 2
def topCountMovies(lstmovies):
    ls.shellSort(lstmovies, topMovies)
    for i in range(1, 11):
        dato = lt.getElement(lstmovies, i)
        print (dato['original_title'] + ": " + dato['vote_count'])
def lowCountMovies(lstmovies):
    ls.shellSort(lstmovies, lowMovies)
    for i in range(1, 11):
        dato = lt.getElement(lstmovies, i)
        print (dato['original_title'] + ": " + dato['vote_count'])
def topAveMovies(lstmovies):
    ls.shellSort(lstmovies, topMoviesAve)
    for i in range(1, 6):
        dato = lt.getElement(lstmovies, i)
        print (dato['original_title'] + ": " + dato['vote_average'])
def lowAveMovies(lstmovies):
    ls.shellSort(lstmovies, lowMoviesAve)
    for i in range(1, 6):
        dato = lt.getElement(lstmovies, i)
        print (dato['original_title'] + ": " + dato['vote_average'])

#Función requerimiento 3
def Conocer_un_director(lst, lst2, criteria):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    t1 = process_time()
    i = 0
    cont = 0
    valor = 0
    print("\n")
    while i < lst2['size']:
        vote = lt.getElement(lst2, i)
        nom = vote["director_name"]
        ids = int(vote["id"])
        if criteria == lt.getElement(lst2, i)["director_name"]:
            j = 0
            while j < lst['size']:
                vote2 = lt.getElement(lst, j)
                ids2 = int(vote2["id"])
                if int(ids) == int(ids2):
                    cont += 1
                    valor += float(vote2["vote_average"])
                    print(vote2["original_title"])
                    j += 1
                else:
                    j += 1
            i += 1
        else:
            i += 1 
    
    print("\nLa cantidad de películas es de: " + str(cont))      
    if cont == 0:
        promedio = valor/1
    else:
        promedio = valor/cont
    print("Su promedio es de: " + str(round(promedio, 2)))    
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    

#Función requerimiento 4

def Conocer_un_actor(lst, lst2, criteria):
    t1 = process_time()
    i = 0
    cont = 0
    valor = 0
    dicc = {}
    print("\n")
    while i < lst2['size']:
        vote = lt.getElement(lst2, i)
        ids = int(vote["id"])
        if ((criteria == lt.getElement(lst2, i)["actor1_name"]) or 
        (criteria == lt.getElement(lst2, i)["actor2_name"]) or 
        (criteria == lt.getElement(lst2, i)["actor3_name"]) or 
        (criteria == lt.getElement(lst2, i)["actor4_name"]) or 
        (criteria == lt.getElement(lst2, i)["actor5_name"])):
            j = 0
            while j < lst['size']:
                vote2 = lt.getElement(lst, j)
                ids2 = int(vote2["id"])
                if int(ids) == int(ids2):
                    cont += 1
                    valor += float(vote2["vote_average"])
                    print(vote2["original_title"])
                    if (vote["director_name"]) in dicc:
                        dicc[vote["director_name"]] += 1
                    else:
                        dicc[vote["director_name"]] = 1  
                    j += 1
                else:
                    j += 1
            i += 1
        else:
            i += 1 
    print("La cantidad de películas es de: " + str(cont))      
    if cont == 0:
        promedio = valor/1
    else:
        promedio = valor/cont
    print("Su promedio es de: " + str(round(promedio, 2)))
    m = (max(dicc.values()))
    for i in dicc:
        if m == dicc[i]:
            print(i)
    t2 = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)

    




# Consola
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()
                lstcasting = loadCasting()
            elif int(inputs[0])==2: #opcion 2
                if lstmovies==None or lt.size(lstmovies)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")   
                else: print("La lista tiene ",lstmovies['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                a = int(input("selecciones una opción: \n" + "1. 10 mejores películas votadas\n"
                + "2. 10 peores películas votadas\n" + "3. 5 mejores películas según su promedio\n"
                + "4. 5 peores películas según su promedio\n" + ": " ))
                if a == 1:
                    topCountMovies(lstmovies)
                elif a == 2:
                    lowCountMovies(lstmovies)
                elif a == 3:
                    topAveMovies(lstmovies)
                elif a == 4:
                    lowAveMovies(lstmovies)
                    
            elif int(inputs[0])==4: #opcion 4
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("La información de su director: \n")
                    criteria =input('Ingrese el nombre del director a buscar: \n')
                    counter= Conocer_un_director(lstmovies, lstcasting, criteria)

            elif int(inputs[0])==5: #opcion 5
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    Conocer_un_actor(lstmovies, lstcasting, criteria)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()