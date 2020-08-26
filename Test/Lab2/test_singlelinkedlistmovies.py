import pytest
from DataStructures.singlelinkedlist import *
from time import process_time
import config
import csv
import random as rd


def cmpfunction(element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst():
    lst = newList(cmpfunction)
    return lst


@pytest.fixture
def movies():
    """
    """
    file = "C:/Users/Netie/Documents/Lab2_202020/Data/Movies/SmallMoviesDetailsCleaned.csv"
    movies = []  # Usando lista interna
    t1_start = process_time()  # tiempo inicial
    print("Cargando archivo ....")
    # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = ";"
    with open(file, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            movies.append(row)

    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    print(movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    lst = newList(cmpfunction)
    for i in range(len(movies)):
        addLast(lst, movies[i])
    return lst


def test_empty(lst):
    assert isEmpty(lst)
    assert size(lst) == 0


def test_addFirst(lst, movies):
    assert size(lst) == 0
    addFirst(lst, movies[34])
    assert size(lst) == 1
    movie = firstElement(lst)
    assert movie == movies[34]
    addFirst(lst, movies[28])
    assert size(lst) == 2
    movie = firstElement(lst)
    assert movie == movies[28]


def test_getElement(lstmovies, movies):
    largo = size(lstmovies)
    pos_alt = rd.randint(1, largo)
    movie = getElement(lstmovies, pos_alt)
    assert movie == movies[pos_alt - 1]
    pos_alt = rd.randint(1, largo)
    movie = getElement(lstmovies, pos_alt)
    assert movie == movies[pos_alt - 1]


def test_removeFirst(lstmovies, movies):
    largo = size(lstmovies)
    removeFirst(lstmovies)
    assert size(lstmovies) == largo - 1
    book = getElement(lstmovies, 1)
    assert book == movies[1]


def test_removeLast(lstmovies, movies):
    largo = len(movies)
    removeLast(lstmovies)
    assert size(lstmovies) == largo - 1
    movie = getElement(lstmovies, largo - 1)
    assert movie == movies[largo - 2]


def test_insertElement(lst, movies):
    assert isEmpty(lst) is True
    assert size(lst) == 0
    insertElement(lst, movies[0], 1)
    assert size(lst) == 1
    insertElement(lst, movies[1], 2)
    assert size(lst) == 2
    insertElement(lst, movies[2], 1)
    assert size(lst) == 3
    book = getElement(lst, 1)
    assert book == movies[2]
    book = getElement(lst, 2)
    assert book == movies[0]


def test_isPresent(lstmovies, movies):
    movie = dict([("id", "No-id"), ("random", 1), ("dict", 2), ("to", 3), ("prove", 4)])
    largo = size(lstmovies)
    pos_alt_1 = rd.randint(1, largo)
    assert isPresent(lstmovies, movies[pos_alt_1]) > 0
    assert isPresent(lstmovies, movie) == 0


def test_deleteElement(lstmovies, movies):
    largo = size(lstmovies)
    pos_alt_1 = rd.randint(1, largo)
    pos = isPresent(lstmovies, movies[pos_alt_1])
    assert pos > 0
    movie = getElement(lstmovies, pos)
    assert movie == movies[pos - 1]
    deleteElement(lstmovies, pos)
    assert size(lstmovies) == largo - 1
    movie = getElement(lstmovies, pos)
    assert movie == movies[pos]


def test_changeInfo(lstmovies, movies):
    largo = size(lstmovies)
    pos_alt_1 = rd.randint(1, largo)
    pos_alt_2 = rd.randint(1, largo)
    movie_pueba = movies[pos_alt_1]
    changeInfo(lstmovies, pos_alt_2, movie_pueba)
    movie = getElement(lstmovies, pos_alt_2)
    assert movie_pueba == movie


def test_exchange(lstmovies, movies):
    largo = size(lstmovies)
    pos_alt_1 = rd.randint(1, largo)
    pos_alt_2 = rd.randint(1, largo)
    movie1 = getElement(lstmovies, pos_alt_1)
    movie2 = getElement(lstmovies, pos_alt_2)
    exchange(lstmovies, pos_alt_1, pos_alt_2)
    assert getElement(lstmovies, pos_alt_1) == movie2
    assert getElement(lstmovies, pos_alt_2) == movie1


def test_addLast(lst, movies):
    largo = len(movies)
    pos_alt_1 = rd.randint(1, largo)
    pos_alt_2 = rd.randint(1, largo)
    assert isEmpty(lst)
    assert size(lst) == 0
    addLast(lst, movies[pos_alt_1])
    assert size(lst) == 1
    addLast(lst, movies[pos_alt_2])
    assert size(lst) == 2
    movie = firstElement(lst)
    assert movie == movies[pos_alt_1]
    movie = lastElement(lst)
    assert movie == movies[pos_alt_2]
