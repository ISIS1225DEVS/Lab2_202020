




import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

list_type = 'ARRAY_LIST'
#list_type = 'SINGLE_LINKED'

lst_movie = lt.newList(list_type)
moviefile = cf.data_dir + 'theMoviesdb/SmallMoviesDetailsCleaned2.csv'


def setUp():
    print('Loading movies')
    loadCSVFile(moviefile, lst_movie)
    print(lst_movie['size'])


def tearDown():
       pass


def loadCSVFile(file, lst,sep=';'):

 
    
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")



    

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['budget'])

def less(element1, element2):
    if float(element1['budget']) < float(element2['budget']):
        return True
    return False

def test_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_movie, less)

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_movie,less)
    while not (lt.isEmpty(lst_movie)):
        x = float(lt.removeLast(lst_movie)['budget'])
        if not (lt.isEmpty(lst_movie)):
            y = float(lt.lastElement(lst_movie)['budget'])
        else:
            break
        assert x >= y













