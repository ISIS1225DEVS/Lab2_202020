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


import config as cf
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos



def compareauthors (Director_name, director):

    return  (Director_name == director['name'] )


def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar todos los libros,
    Adicionalmente, crea una lista vacia para los autores y una lista vacia para los 
    generos.   Retorna el catalogo inicializado.
    """
    catalog = {'Peliculas':None, 'Directores':None, 'Categorias': None}
    catalog['Peliculas'] = lt.newList('ARRAY_LIST')
    catalog['Directores'] = lt.newList('ARRAY_LIST')
    catalog['Categorias'] = lt.newList('ARRAY_LIST')
    return catalog


def newDirector (name):
    """
    Crea una nueva estructura para modelar los libros de un autor y su promedio de ratings
    """
    director = {'name':"", "Peliculas":None,  "vote_average":0}
    director ['name'] = name
    director ['Peliculas'] = lt.newList('ARRAY_LIST')
    return director


def newCategoria (name):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido 
    marcados con dicho tag.  Se guarga el total de libros y una lista con 
    dichos libros.
    """
    cat = {'name':'', 'numero_Peliculas':0, 'peliculas':None, 'count':0.0 }
    cat ['name'] = name
    cat ['peliculas'] = lt.newList ()
    return tag


# Funciones para agregar informacion al catalogo

def add_Movie_director (catalog, director_name, pelicula, compareauthors):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias a los libros de dicho autor
    """
    directores = catalog['Directores']
    posauthor = lt.isPresent (directores, director_name, compareauthors)
    if posauthor > 0:
        director = lt.getElement (directores,posauthor)    
    else:
        director = newDirector(director_name)
        lt.addLast (directores, director)
    lt.addLast (director['Peliculas'], pelicula)
    if (director['vote_average']==0.0):
        director['vote_average']= float (pelicula['vote_average'])  
    else:
        director['vote_average'] = (director['vote_average'] + float(pelicula['vote_average']) ) / 2



def addCategoria (catalog, categoria):
    """
    Adiciona un tag a la lista de tags
    """
    t = newCategoria (categoria['name'])
    lt.addLast (catalog['Categorias'], t)



def addBookTag (catalog, tag, comparefunction, comparegoodreadsid):
    """
    Agrega una relación entre un libro y un tag asociado a dicho libro
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    pos = lt.isPresent(catalog['tags'], tagid, comparefunction)
    if pos:
        tagbook = lt.getElement (catalog['tags'], pos)
        tagbook ['total_books'] += 1
        tagbook ['count'] += int (tag['count'])
        posbook = lt.isPresent(catalog['books'], bookid, comparegoodreadsid)
        if posbook:
            book =  lt.getElement (catalog['books'], posbook) 
            lt.addLast (tagbook['books'], book)


# Funciones de consulta

def getBooksByAuthor (catalog, director_name, compareauthors):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    directore = lt.isPresent (catalog['Directores'], director_name, compareauthors)
    if directore > 0:
        direc= lt.getElement (catalog['Directores'], directore)
        return direc
    return None