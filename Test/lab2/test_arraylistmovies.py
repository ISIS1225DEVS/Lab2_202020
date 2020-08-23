import pytest 
import config 
import csv
from DataStructures import arraylist as slt
from DataStructures import listiterator as it

def cmpfunction (element1, element2):
    if element1["movie_id"] == element2["movie_id"]:
        return 0
    elif element1["movie_id"] < element2["movie_id"]:
        return -1
    else:
        return 1

@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst



def loadCSVFile():
    lista=[]
    lst = slt.newList()

    moviesfile = 'theMoviesdb/MoviesCastingRaw-small.csv'
    moviesfile2 = 'theMoviesdb/SmallMoviesDetailsCleaned.csv'
    sep = ";"
    dialect = csv.excel()
    dialect.delimiter=sep
    assert (slt.size(lst)==0), "La lista no empieza en cero"
    try:
        with open(moviesfile, encoding = "utf-8") as csvfile:
            reader= csv.DictReader(csvfile,dialect=dialect)
            for row in reader:
                lista.append(row)
                slt.addLast(lst, row)

    except:
        assert False, "Se presento un error al cargar el archivo"
    assert len(lista) == slt.size(lst), "Son diferentes tamaños"

    for i in range (len(lista)):
        assert slt.getElement(lst, i*1)== lista[i], "las listas no estan en el mismo orden"
    
