import pytest
import csv
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

def test_carga():
    lista=[]
    lst=lt.newList("ARRAY_LIST")

    file="Data/test.csv"
    sep=";"
    dialect=csv.excel()
    dialect.delimiter=sep

    assert (lt.size(lst)==0),"la lista no empieza en 0"


    try:j
        with open (file,encoding="utf-8") as csvfile:
            reader=csv.DictReader(csvfile, dialect=dialect)

            for row in reader:
                lista.append(row)
                lt.addLast(lst,row)

    except: 
        assert False, "Error"

    assert len(lista)==lt.size(lst), "Son diferentes tamaños"
    for i in range (len(lista)):
        assert lista[i]==lt.getElement(lst,i+1)
    return (lst)

print (test_carga())