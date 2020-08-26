"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los 
 *Andes 
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
  Este módulo es una aplicación básica con un menú de opciones para cargar 
  datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import selectionsort as sort

from time import process_time 

def less(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True
    return False

def greater(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False

def loadCSVFile (file1, file2, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro,
        si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
    
        while
        # with open(file1, encoding="utf-8") as csvfile1, open(file2, encoding="utf-8") as csvfile2:
        #     spamreader1 = csv.DictReader(csvfile, dialect=dialect)
        #     spamreader2 = csv.DictReader(csvfile, dialect=dialect)
        #     for i in spamreader2:
        #         spamreader1[i] = spamreader2[i]
        #     for row in spamreader1: 
        #         lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    print(lt.getElement(lst, 1))
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Clasificar peliculas por votación")
    print("0- Salir")

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
            la cantidad de veces ue aparece un elemento con el criterio
            definido
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
            if criteria.lower() in element[column].lower():  
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una 
    columna dada
    """
    t1_start = process_time() #tiempo inicial
    counter = 0
    for i in lst:
        if criteria in i[column]:
            counter += 1
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el 
    criterio
    """
    NewList = []
    t1_start = process_time() #tiempo inicial
    sort.selectionSort(lst, function)
    for i in range(elements):
        NewList.append(lt.getElement(lst, i))
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos\n")
    return NewList

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos
    adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde
    el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                # lista = loadCSVFile("Data/theMoviesdb/AllMoviesCastingRaw.csv") 
                # lista = loadCSVFile("Data/theMoviesdb/AllMoviesDetailsCleaned.csv")
                # lista = loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-small.csv")
                # lista = loadCSVFile("Data/theMoviesdb/SmallMoviesDetailsCleaned.csv")
                lista = loadCSVFile("Data/theMoviesdb/short.csv", "Data/theMoviesdb/shortcasting.csv")
                print("Datos cargados, ",lista['size']," elementos cargados")
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
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria1 = input('Ingrese 0 para las de mayor promedio o 1 para las de menor promedio:\n')
                    cant1 = input('Ingrese la cantidad de películas que desea ver por por el promedio de calificación:\n')
                    criteria2 = input('Ingrese 0 para las de mayor cantidad de votos o 1 para las de menor cantidad:\n')
                    cant2 = input('Ingrese la cantidad de películas que desea ver por por la cantidad de votos:\n')
                    # try:
                    if int(criteria1[0]) == 0:
                        prom = orderElementsByCriteria(greater, 'vote_average', lista, int(cant1))
                    elif int(criteria1[0]) == 1:
                        prom = orderElementsByCriteria(less, 'vote_average', lista, int(cant1))
                    if int(criteria2[0]) == 0:
                        count = orderElementsByCriteria(greater, 'vote_count', lista, int(cant2))
                    elif int(criteria2[0]) == 1:
                        count = orderElementsByCriteria(less, 'vote_count', lista, int(cant2))
                    print('\nLos resultados por promedio son:')
                    print('-' * 30)
                    for i in prom:
                        print(i['title'], i['vote_average'])
                    print('\nLos resultados por cantidad de votos son:')
                    print('-' * 30)
                    for i in count:
                        print(i['title'], i['vote_average'])
                    # except:
                    #     print('Ha ocurrido un error al ingresar los parametros')
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()