#imports

from DataStructures import listiterator as it
from DataStructures import liststructure as lt

#sorted

def lessfunction(element1, element2, criteria):
    condicion=False
    element1=element1[criteria]
    element2=element2[criteria]
    if element1 <= element2:
        condicion=True
    return condicion

def greaterfunction(element1, element2, criteria):
    condicion=False
    element1=element1[criteria]
    element2=element2[criteria]
    if element1 >= element2:
        condicion=True
    return condicion
    
#Funciones de apoyo

def findmoviesDirector(director_name, lst):
    """
    retorna:
        -lista de peliculas del director pasado por parametro.
    """
    info_movies=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie= it.next(iterator)
        if director_name.lower() in movie['director_name'].lower():
            info_movies.append(movie["id"])
    return info_movies

def findmoviesActor(actor_name, lst):
    info_movies=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        if actor_name.lower() in movie['actor1_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor2_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor3_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor4_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor5_name'].lower():
            info_movies.append(movie)
    return info_movies
    
def findmoviesGenre(genre, lst):
    """
    Retorna:
        -lista de peliculas que tienen en su genero 
    """
    info_movies=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        if genre.lower() in movie['genres'].lower():
            info_movies.append(movie)
    return info_movies