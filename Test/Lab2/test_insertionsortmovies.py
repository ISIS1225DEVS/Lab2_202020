"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 *
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


import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv
from DataStructures import arraylist as slt
from DataStructures import liststructure as lt


#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

lst_books = lt.newList(list_type)



@pytest.fixture
def test_carga ():
    lista=[]
    lst= lt.newList()

    file= 'Data/GoodReads/MoviesCastingRaw-Small.csv'
    sep=';'
    dialect=csv.excel()
    dialect.delimiter=sep

    assert (lt.size(lst)==0), "La lista no empieza en cero"
    try:
        with open (file, encoding="utf-8")as csvfile:
            reader= csv.DictReader(csvfile, dialect=dialect)

            for row in reader:
                lista.append(row)
                lt.addLast(lst, row)

    except:
        assert False, "Se presento un error al cargar el archivo"

    assert len(lista)== lt.size(lst), "Son difererentes tamanios"

    for i in range(len(lista)):
        assert lt.getElement(lst, i+1)==lista[i], "Las listas no estan en el mismo orden "


def setUp():
    print('Loading books')
    loadCSVFile(lista, lst_books)
    print(lst_books['size'])


def tearDown():
       pass


def loadCSVFile(file, lst):
    input_file = csv.DictReader(open(file, encoding = "utf-8"))
    for row in input_file:
        lt.addLast(lst, row)

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['goodreads_book_id'])

def less(element1, element2):
    if int(element1['goodreads_book_id']) < int(element2['goodreads_book_id']):
        return True
    return False

def test_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_books, less)

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_books,less)
    while not (lt.isEmpty(lst_books)):
        x = int(lt.removeLast(lst_books)['goodreads_book_id'])
        if not (lt.isEmpty(lst_books)):
            y = int(lt.lastElement(lst_books)['goodreads_book_id'])
        else:
            break
        assert x > y

