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



