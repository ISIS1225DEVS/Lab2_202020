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
from Sorting import insertionsort as sort
import Moviecatalog as mg

from time import process_time 

def less(element1, element2):
    if float(element1["vote_count"]) < float(element2["vote_count"]):
        return True

def less2(element1, element2):
    if float(element1["vote_average"]) < float(element2["vote_average"]):
        return True
    return False

def greater1(element1, element2):
    if float(element1['vote_count']) > float(element2['vote_count']):
        return True
    return False

def greater2(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False

def loadCSVFile (file,file2, sep=";"):
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
    catalog=mg.newCatalog()#Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    if 1:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                lt.addLast(catalog["Peliculas"],row)
        lista=[]
        with open(file2, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row2 in spamreader:
                nombre=row2["director_name"]
                id1=row2["id"]
                iterador= it.newIterator(catalog["Peliculas"])
                while it.hasNext(iterador):
                    pelicula= it.next(iterador)
                    id2=pelicula["id"]
                    if id1==id2:
                        mg.add_Movie_director(catalog,nombre,pelicula, mg.compareauthors)
       
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    count=1
    print(lt.size(catalog["Directores"]))

    iterador3 = it.newIterator(catalog["Directores"])
    while it.hasNext(iterador3) and count==1:
        director=it.next(iterador3) 
        print(director["name"]["Peliculas"])
        count+=1

    catalog["Directores"]
    return catalog





def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- ordenar elementos de una columna")
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

def countElementsByCriteria(criteria, column, lst, lst2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:

        t1_start = process_time() #tiempo inicial
        counter=0
        iterador= it.newIterator(lst)
        while  it.hasNext(iterador):
            element = it.next(iterador)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave
                id1=element["id"]
                iterator2= it.newIterator(lst2)
                while  it.hasNext(iterator2):
                     element2 = it.next(iterator2)
                     id2=element2["id"]
                     if id1 == id2:
                         if float(element2["vote_average"]) >= 6:
                             counter+=1
        t1_stop = process_time() #tiempo final

    return counter

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:

        t1_start = process_time() #tiempo inicial
        lista=lt.newList()
        if column=="vote_count" and function.lower() == "acendente" :
            sort.insertionSort(lst,less)
            iterador= it.newIterator(lst)
            counter=1
            while it.hasNext(iterador) and counter<=int(elements):
                element=it.next(iterador)
                lt.addLast(lista,element)
                
                counter+=1
            hola=lt.subList(lst,1,int(elements))
        elif column=="vote_count" and function.lower() == "decendente" :
            sort.insertionSort(lst,greater1)
            iterador= it.newIterator(lst)
            counter=1
            while it.hasNext(iterador) and counter<=int(elements):
                element=it.next(iterador)
                lt.addLast(lista,element)
                counter+=1

        elif column=="vote_average" and function.lower() == "acendente":
            sort.insertionSort(lst,less2)
            iterador= it.newIterator(lst)
            counter=1
            while it.hasNext(iterador) and counter<=int(elements):
                element=it.next(iterador)
                lt.addLast(lista,element)
                counter+=1
        
        elif column=="vote_average" and function.lower() == "decendente":
            sort.insertionSort(lst,greater2)
            iterador= it.newIterator(lst)
            counter=1
            while it.hasNext(iterador) and counter<=int(elements):
                element=it.next(iterador)
                lt.addLast(lista,element["vote_average"])
                counter+=1

        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    print(lt.size(hola))
    return hola

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
            
                lista = loadCSVFile("Data/test2.csv","Data/test3.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lt.size(lista["Peliculas"])," elementos cargados")
                
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    columna=input('Ingrese la columna de interes\n')    
                    counter=countElementsFilteredByColumn(criteria, columna, lista2) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,"director_name",lista2,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    column=input('Ingrese la columna a organizar\n')
                    elements=input('Ingrese el numero de datos a mostrar\n')
                    function=input("ingrese si quiere los datos acendentes o decendentes\n")
                    organizar=orderElementsByCriteria(function, column, lista, elements)
                    print("estos son los primeros",elements,"elementos de la lista de acuerdo a",column,":",organizar)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()