import pytest 
import config 
import csv
from DataStructures import arraylist as slt

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
#Cargar base de datos
#lst()
#lst_movies = slt.newList(cmpfunction)
moviesfile = config.data_dir + 'theMoviesdb/MoviesCastingRaw-small.csv'
moviesfile2 = config.data_dir + 'theMoviesdb/SmallMoviesDetailsCleaned.csv'
#lst = slt.newList(cmpfunction)
print(type(lst))

def loadCSVFile(file1,file2, lst,sep =";"):
    dialect = csv.excel()
    dialect.delimiter=sep
    input_file1 = csv.DictReader(open(file1, encoding = "utf-8"),dialect=dialect)
    input_file2 = csv.DictReader(open(file2, encoding = "utf-8"),dialect=dialect)
    
    for row in input_file1:
        slt.addLast(lst, row)
    pos=0
    for row in input_file2: 
        lst["elements"][pos].update({"Details_claned":row})
        pos+=1
  


         

#loadCSVFile(moviesfile,moviesfile2,lst)

#print(lst["elements"][1]["Details_claned"]["genres"])







@pytest.fixture
def books ():
    books = []
    books.append({'book_id':'1', 'book_title':'Title 1', 'author':'author 1'})
    books.append({'book_id':'2', 'book_title':'Title 2', 'author':'author 2'})
    books.append({'book_id':'3', 'book_title':'Title 3', 'author':'author 3'})
    books.append({'book_id':'4', 'book_title':'Title 4', 'author':'author 4'})
    books.append({'book_id':'5', 'book_title':'Title 5', 'author':'author 5'})
    print (books[0])
    return books

