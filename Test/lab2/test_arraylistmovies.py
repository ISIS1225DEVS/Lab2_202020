import pytest 
import config 
import csv
from DataStructures import arraylist as slt

Datos_agregar=loadCSV('Data\est.csv', cmpfunction, "test")

movies=loadCSV('Data\SmallMoviesDetailsCleaned.csv', cmpfunction, "movies")

lst=lst()

@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst

def loadCSV(file, cmpfunction,name,sep=','):
    name=lst()
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding='utf-8') as csvfile:
            reader=csv.DictReader(csvfile, dialect=dialect)
            for row in reader:
                slt.addLast(movies, row)
    except:
        print('Ocurrio un error en la carga de archivos')
    t1_stop=process_time()
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return movies
    assert lst != 0



def cmpfunction(element1, element2):
    if element1['id'] == element2['id']:
        return 0
    elif element1['id'] < element2['id']:
        return -1
    else:
        return 1


def test_empty (lst):
    assert slt.isEmpty(movies) == True
    assert slt.size(movies) == 0 



def test_addFirst (movies, Datos_agregar):
    size=slt.size(movies)
    slt.addFirst (lst, Datos_agregar['elements'][0])
    assert slt.size(movies) == size+1 
    slt.addFirst (movies, Datos_agregar['elements'][1])
    assert slt.size(movies) == size+2
    movie = slt.firstElement(movies)
    assert movie == Datos_agregar['elements'][1]




def test_addLast (movies, Datos_agregar):
    assert slt.isEmpty(lst) == True
    size= slt.size(movies) == 0
    slt.addLast (movies, Datos_agregar['elements'][2])
    assert slt.size(movies) == size+1
    slt.addLast (movies, Datos_agregar['elements'][3])
    assert slt.size(movies) == size+2
    movie = slt.firstElement(movies)
    assert movie == Datos_agregar['elements'][1]
    movie = slt.lastElement(movies)
    assert movie == Datos_agregar['elements'][3]




def test_getElement(movies, Datos_agregar):
    book = slt.getElement(movies, 1)
    assert book ==  Datos_agregar['elements'][0]





def test_removeFirst (movies, Datos_agregar):
    size=slt.size(movies)
    slt.removeFirst(movies)
    assert slt.size(movies) == (size-1)
    movie= slt.firstElement(movies)
    assert movie == Datos_agregar['elements'][0]



def test_removeLast (movies, Datos_agregar):
    size=slt.size(movies) 
    slt.removeLast(movies)
    assert slt.size(movies) == size-1
    movie = slt.getElement(movies, size-1)
    assert movie  == Datos_agregar['elements'][2]



def test_insertElement (movies, Datos_agregar):
    size= slt.size(movies)
    slt.insertElement (movies, Datos_agregar['elements'][0], 2)
    assert slt.size(lst) == size+1
    slt.insertElement (movies, Datos_agregar['elements'][1], 3)
    assert slt.size(lst) == size+2
    movie = slt.getElement(movies, 2)
    assert movie == Datos_agregar['element'][0]
    movie = slt.getElement(movie, 3)
    assert movie == Datos_agregar['element'][1]



def test_isPresent (movies, Datos_agregar):
    movie=slt.getElement(Datos_agregar, 1)
    print(slt.isPresent (movies, movie))
    assert slt.isPresent (movies, movie) > 0
    assert slt.isPresent (movies, movie) == 0
    


def test_deleteElement (movies, Datos_agregar):
    pos = slt.isPresent (movies, )
    assert pos > 0
    book = slt.getElement(lstbooks, pos)
    assert book == books[2]
    slt.deleteElement (lstbooks, pos)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, pos)
    assert book == books[3]


def test_changeInfo (movies, Datos_agregar):
    movie=slt.getElement(Datos_agregar, 3)
    slt.changeInfo (movies, 1, movie)
    movie_inf = slt.getElement(movies, 1)
    assert movie == movie_inf


def test_exchange (movies, Datos_agregar):
    book1 = slt.getElement(lstbooks, 1)
    book5 = slt.getElement(lstbooks, 5)
    slt.exchange (lstbooks, 1, 5)
    assert slt.getElement(lstbooks, 1) == book5
    assert slt.getElement(lstbooks, 5) == book1