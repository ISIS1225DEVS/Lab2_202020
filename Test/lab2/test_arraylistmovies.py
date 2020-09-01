
import pytest 
import config 
import csv

from ADT import list as lt



@pytest.fixture
def loadCSVFile (file="Data/SmallMoviesDetailsCleaned.csv", sep=";"):
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
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

@pytest.fixture 
def lstmoviesDetails (file="Data/SmallMoviesDetailsCleaned.csv", sep=";"):
    lst = lt.newList("ARRAY_LIST")
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

@pytest.fixture
def lst ():
    lst = lt.newList('ARRAY_LIST')
    return lst


def test_empty (lst):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0




def test_addFirst (lst, loadCSVFile):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addFirst (lst, loadCSVFile["elements"][1])
    assert lt.size(lst) == 1
    lt.addFirst (lst, loadCSVFile["elements"][2])
    assert lt.size(lst) == 2
    detail = lt.firstElement(lst)
    assert detail == loadCSVFile["elements"][2]




def test_addLast (lst, loadCSVFile):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addLast (lst, loadCSVFile["elements"][1])
    assert lt.size(lst) == 1
    lt.addLast (lst, loadCSVFile["elements"][2])
    assert lt.size(lst) == 2
    detail = lt.firstElement(lst)
    assert detail == loadCSVFile["elements"][1]
    detail = lt.lastElement(lst)
    assert detail == loadCSVFile["elements"][2]




def test_getElement(lstmoviesDetails, loadCSVFile):
    detail = lt.getElement(lstmoviesDetails, 1)
    assert detail == loadCSVFile["elements"][0]
    detail = lt.getElement(lstmoviesDetails, 5)
    assert detail == loadCSVFile["elements"][4]




def test_removeFirst (lstmoviesDetails, loadCSVFile):
    assert lt.size(lstmoviesDetails) == 2000
    lt.removeFirst(lstmoviesDetails)
    assert lt.size(lstmoviesDetails) == 1999
    detail = lt.getElement(lstmoviesDetails, 1)
    assert detail  == loadCSVFile["elements"][1]



def test_removeLast (lstmoviesDetails, loadCSVFile):
    assert lt.size(lstmoviesDetails) == 2000
    lt.removeLast(lstmoviesDetails)
    assert lt.size(lstmoviesDetails) == 1999
    detail = lt.getElement(lstmoviesDetails, 1999)
    assert detail  == loadCSVFile["elements"][1998]



def test_insertElement (lst, loadCSVFile):
    assert lt.isEmpty(lst) is True
    assert lt.size(lst) == 0
    lt.insertElement (lst, loadCSVFile["elements"][0], 1)
    assert lt.size(lst) == 1
    lt.insertElement (lst, loadCSVFile["elements"][1], 2)
    assert lt.size(lst) == 2
    lt.insertElement (lst, loadCSVFile["elements"][2], 1)
    assert lt.size(lst) == 3
    detail = lt.getElement(lst, 1)
    assert detail == loadCSVFile["elements"][2]
    detail = lt.getElement(lst, 2)
    assert detail == loadCSVFile["elements"][0]



def test_isPresent (lstmoviesDetails, loadCSVFile):
    detail = {'id':'10', 'budget':'Title 10', 'genres':'author 10', "imdb_id":"","original_language":"","original_title":"","overview":"","popularity":"","production_companies":"","production_countries":"","release_date":"","revenue":"","runtime":"","spoken_languages":"","status":"","tagline":"","title":"","vote_average":"","vote_count":"","production_companies_number":"","production_countries_number":"","spoken_languages_number":""}
    assert lt.isPresent (lstmoviesDetails, loadCSVFile["elements"][2]) > 0
    assert lt.isPresent (lstmoviesDetails, detail) == 0
    


def test_deleteElement (lstmoviesDetails, loadCSVFile):
    pos = lt.isPresent (lstmoviesDetails, loadCSVFile["elements"][2])
    assert pos > 0
    detail = lt.getElement(lstmoviesDetails, pos)
    assert detail == loadCSVFile["elements"][2]
    lt.deleteElement (lstmoviesDetails, pos)
    assert lt.size(lstmoviesDetails) == 4
    detail = lt.getElement(lstmoviesDetails, pos)
    assert detail == loadCSVFile["elements"][3]



def test_changeInfo (lstmoviesDetails):
    movie10 = {"id":'10', 'budget':'Title 10', 'genres':'author 10', "imdb_id":"","original_language":"","original_title":"","overview":"","popularity":"","production_companies":"","production_countries":"","release_date":"","revenue":"","runtime":"","spoken_languages":"","status":"","tagline":"","title":"","vote_average":"","vote_count":"","production_companies_number":"","production_countries_number":"","spoken_languages_number":""}
    lt.changeInfo (lstmoviesDetails, 1, movie10)
    detail = lt.getElement(lstmoviesDetails, 1)
    assert movie10 == detail


def test_exchange (lstmoviesDetails, loadCSVFile):
    movie1 = lt.getElement(lstmoviesDetails, 1)
    movie5 = lt.getElement(lstmoviesDetails, 5)
    lt.exchange (lstmoviesDetails, 1, 5)
    assert lt.getElement(lstmoviesDetails, 1) == movie5
    assert lt.getElement(lstmoviesDetails, 5) == movie1
