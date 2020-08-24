import config
import pytest
from sorting import shellsort as shsort 
from DataStructures import listiterator as ls
from ADT import list as lt
import Support as supp
from test_arraylistmovies import load_arraylist
from test_singlelinkedlistmovies import load_singlelinkedlist

def test_insertionsortSingleLinkedList(load_singlelinkedlist):
    (lista_movies_casting, lista_movies_details) = load_singlelinkedlist
    shsort.shellsort(lista_movies_casting,supp.less)
    shsort.shellsort(lista_movies_details,supp.less)



def test_insertionsortArray(load_arraylist):
    
    (lista_movies_casting, lista_movies_details) = load_arraylist
    shsort.shellsort(lista_movies_casting,supp.less)
    shsort.shellsort(lista_movies_details,supp.less)