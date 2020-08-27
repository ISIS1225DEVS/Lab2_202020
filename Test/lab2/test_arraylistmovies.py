import config
import pytest
import Support as supp


Movies_details= "theMoviesdb/SmallMoviesDetailsCleaned.csv"
Movies_Casting= "theMoviesdb/MoviesCastingRaw.csv"

ltt= []
ltt2=[]
def test_LoadArrayList():
    
    lista_movies_details= supp.loadCSVFile1(Movies_details,ltt)
    lista_movies_casting= supp.loadCSVFile1(Movies_Casting,ltt2)

    return lista_movies_casting, lista_movies_details

@pytest.fixture
def load_arraylist():
    return test_LoadArrayList()