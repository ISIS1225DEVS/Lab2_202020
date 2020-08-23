
import pytest 
import config 


from ADT import list as lt


"""def cmpfunction (element1, element2):
    if element1['book_id'] == element2['book_id']:
        return 0
    elif element1['book_id'] < element2['book_id']:
        return -1
    else:
        return 1"""

@pytest.fixture 
def lstmoviesDetails (file="Data/SmallMoviesDetailsCleaned.csv"):
    lst = lt.newList("ARRAY_LIST")
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.addLast(lst,row)
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




def test_addFirst (lst, books):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addFirst (lst, books[1])
    assert lt.size(lst) == 1
    lt.addFirst (lst, books[2])
    assert lt.size(lst) == 2
    book = lt.firstElement(lst)
    assert book == books[2]




def test_addLast (lst, books):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addLast (lst, books[1])
    assert lt.size(lst) == 1
    lt.addLast (lst, books[2])
    assert lt.size(lst) == 2
    book = lt.firstElement(lst)
    assert book == books[1]
    book = lt.lastElement(lst)
    assert book == books[2]




def test_getElement(lstbooks, books):
    book = lt.getElement(lstbooks, 1)
    assert book == books[0]
    book = lt.getElement(lstbooks, 5)
    assert book == books[4]




def test_removeFirst (lstbooks, books):
    assert lt.size(lstbooks) == 5
    lt.removeFirst(lstbooks)
    assert lt.size(lstbooks) == 4
    book = lt.getElement(lstbooks, 1)
    assert book  == books[1]



def test_removeLast (lstbooks, books):
    assert lt.size(lstbooks) == 5
    lt.removeLast(lstbooks)
    assert lt.size(lstbooks) == 4
    book = lt.getElement(lstbooks, 4)
    assert book  == books[3]



def test_insertElement (lst, books):
    assert lt.isEmpty(lst) is True
    assert lt.size(lst) == 0
    lt.insertElement (lst, books[0], 1)
    assert lt.size(lst) == 1
    lt.insertElement (lst, books[1], 2)
    assert lt.size(lst) == 2
    lt.insertElement (lst, books[2], 1)
    assert lt.size(lst) == 3
    book = lt.getElement(lst, 1)
    assert book == books[2]
    book = lt.getElement(lst, 2)
    assert book == books[0]



def test_isPresent (lstbooks, books):
    book = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    assert lt.isPresent (lstbooks, books[2]) > 0
    assert lt.isPresent (lstbooks, book) == 0
    


def test_deleteElement (lstbooks, books):
    pos = lt.isPresent (lstbooks, books[2])
    assert pos > 0
    book = lt.getElement(lstbooks, pos)
    assert book == books[2]
    lt.deleteElement (lstbooks, pos)
    assert lt.size(lstbooks) == 4
    book = lt.getElement(lstbooks, pos)
    assert book == books[3]



def test_changeInfo (lstbooks):
    book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    lt.changeInfo (lstbooks, 1, book10)
    book = lt.getElement(lstbooks, 1)
    assert book10 == book


def test_exchange (lstbooks, books):
    book1 = lt.getElement(lstbooks, 1)
    book5 = lt.getElement(lstbooks, 5)
    lt.exchange (lstbooks, 1, 5)
    assert lt.getElement(lstbooks, 1) == book5
    assert lt.getElement(lstbooks, 5) == book1