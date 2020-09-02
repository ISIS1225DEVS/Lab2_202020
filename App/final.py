"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 
"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""
 
import config as cf
import sys
import csv
 
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as shell
 
from time import process_time 
 
 
 
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking por genero")
    print("0- Salir")
 
 
 
 
def compareRecordIds (id, record):
    if int(id) == int(record['id']):
        return 0
    elif int(id) > int(record['id']):
        return 1
    return -1
 
 
# Cargar Datos
def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst
 
def loadCSVDirectors (file, cmpfunction): 
    listacast = lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter= ";"
    with open(file, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, dialect=dialect)
        for elemento in reader: 
            lugar = lt.isPresent(listacast,elemento["director_name"])
            if lugar:
                director = lt.getElement(listacast,lugar)
                lt.addFirst ((director["movies"]), elemento["id"])
 
            else:
                director = {"name":None , "movies":None}
                director["name"] = elemento["director_name"]
                director["movies"] = lt.newList("SINGLE_LINKED")
                lt.addFirst((director["movies"]), elemento["id"])
                lt.addLast (listacast, director)
    return listacast
 
def loadCSVGenres (file, cmpfunction):
    lstGenres = lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row:
                genres = elemento["genres"]
                genres = genres.replace("|"," ")
                genres = genres.split()
                for i in genres:
                    pos = lt.isPresent(lstGenres, i )
                    if  pos:
                        genre = lt.getElement(lstGenres,pos)
                        lt.addFirst(genre["lstMovies"],elemento["id"])
                    else:
                        genre = {"name": None, "lstMovies":None}
                        genre["name"] = i
                        genre ["lstMovies"] = lt.newList("SINGLE_LINKED")
                        lt.addFirst(genre["lstMovies"], elemento["id"])
                        lt.addLast(lstGenres, genre)
    return lstGenres
 
def loadCSVActors (file,cmpfunction):
    lstActors = lt.newList("ARRAY_LIST",cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row:
                pos = lt.isPresent(lstActors, elemento["actor1_name"])
                if pos:
                    actor = lt.getElement(lstActors,pos)
                    lt.addFirst(actor["movies_id"],elemento["id"])
                    actor["colabs"].append(elemento["director_name"])                 
                else:
                    actor = {"name": None, "movies_id":None, "colabs:":None}
                    actor["name"] = elemento["actor1_name"]
                    actor["movies_id"] = lt.newList("SINGLE_LINKED")
                    actor["colabs"] = []
                    actor["colabs"].append(elemento["director_name"])
                    lt.addFirst(actor["movies_id"], elemento["id"])
                    lt.addLast(lstActors,actor)
                pos = lt.isPresent(lstActors, elemento["actor2_name"])
                if pos:
                    actor = lt.getElement(lstActors,pos)
                    lt.addFirst(actor["movies_id"],elemento["id"])
                    actor["colabs"].append(elemento["director_name"])                 
                else:
                    actor = {"name": None, "movies_id":None, "colabs:":None}
                    actor["name"] = elemento["actor2_name"]
                    actor["movies_id"] = lt.newList("SINGLE_LINKED")
                    actor["colabs"] = []
                    actor["colabs"].append(elemento["director_name"])
                    lt.addFirst(actor["movies_id"], elemento["id"])
                    lt.addLast(lstActors,actor)
                pos = lt.isPresent(lstActors, elemento["actor3_name"])
                if pos:
                    actor = lt.getElement(lstActors,pos)
                    lt.addFirst(actor["movies_id"],elemento["id"])
                    actor["colabs"].append(elemento["director_name"])                 
                else:
                    actor = {"name": None, "movies_id":None, "colabs:":None}
                    actor["name"] = elemento["actor3_name"]
                    actor["movies_id"] = lt.newList("SINGLE_LINKED")
                    actor["colabs"] = []
                    actor["colabs"].append(elemento["director_name"])
                    lt.addFirst(actor["movies_id"], elemento["id"])
                    lt.addLast(lstActors,actor)
                pos = lt.isPresent(lstActors, elemento["actor4_name"])
                if pos:
                    actor = lt.getElement(lstActors,pos)
                    lt.addFirst(actor["movies_id"],elemento["id"])
                    actor["colabs"].append(elemento["director_name"])                 
                else:
                    actor = {"name": None, "movies_id":None, "colabs:":None}
                    actor["name"] = elemento["actor4_name"]
                    actor["movies_id"] = lt.newList("SINGLE_LINKED")
                    actor["colabs"] = []
                    actor["colabs"].append(elemento["director_name"])
                    lt.addFirst(actor["movies_id"], elemento["id"])
                    lt.addLast(lstActors,actor)
                pos = lt.isPresent(lstActors, elemento["actor5_name"])
                if pos:
                    actor = lt.getElement(lstActors,pos)
                    lt.addFirst(actor["movies_id"],elemento["id"])
                    actor["colabs"].append(elemento["director_name"])                 
                else:
                    actor = {"name": None, "movies_id":None, "colabs:":None}
                    actor["name"] = elemento["actor5_name"]
                    actor["movies_id"] = lt.newList("SINGLE_LINKED")
                    actor["colabs"] = []
                    actor["colabs"].append(elemento["director_name"])
                    lt.addFirst(actor["movies_id"], elemento["id"])
                    lt.addLast(lstActors,actor)

    return lstActors
 
def loadMoviesDetails ():
    lst = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst
 
def loadMoviesCasting ():
    lst = loadCSVFile("Data/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst
 
def loadDirectors ():
    lst = loadCSVDirectors("Data/MoviesCastingRaw-small.csv", compareDirectors)
    return lst
 
def loadGenres():
    lst = loadCSVGenres("Data/SmallMoviesDetailsCleaned.csv",compareGenres) 
    return lst
 
def loadActors ():
    lst = loadCSVActors("Data/MoviesCastingRaw-small.csv",compareActors)
    return lst
#Comparaciones
def compareCountBest (movie1, movie2):
    if float(movie1["vote_count"]) > float(movie2["vote_count"]):
        return True
    return False
 
def compareCountWorst (movie1, movie2):
    if float(movie1["vote_count"]) < float(movie2["vote_count"]):
        return True
    return False
 
def compareAverageBest (movie1, movie2):
    if float(movie1["vote_average"]) > float(movie2["vote_average"]):
        return True
    return False
 
def compareAverageWorst (movie1, movie2):
    if float(movie1["vote_average"]) < float(movie2["vote_average"]):
        return True
    return False
 
def compareDirectors (name, director):
    if director["name"] == name:
        return 0
    elif director["name"] > name:
        return 1 
    return -1
 
def compareActors (name,actor):
    if actor["name"] == name:
        return 0
    elif actor["name"] > name:
        return 1 
    return -1
 
def compareGenres (name,genre):
    if genre["name"] == name:
            return 0
    elif genre["name"] > name:
        return 1 
    return -1
#Funciones
def topBestCount (lst, numero, i):#Vote_count
    shell.shellSort(lst, compareCountBest)
    sumatoria = 0
    counter = 0
    for x in range(0+i, numero):
        movie = lt.getElement(lst, x)
        sumatoriaCount = sumatoria + float(movie["vote_count"])
        sumatoriaAverage = sumatoria + float(movie["vote_average"])
        counter = counter + 1
        print(movie["title"])      
    promedioCount = sumatoriaCount/counter
    promedioAverage = sumatoriaAverage/counter
    if i == 1:
        print("Promedio de votos del ranking: "+ str(round(promedioCount,1)))
        print("Promedio de calificación del ranking: "+str(round(promedioAverage,1)))

def topWorstCount (lst, numero, i): #Vote_count
    shell.shellSort(lst, compareCountWorst)
    sumatoria = 0
    counter = 0
    for x in range(0+i, numero):
        movie = lt.getElement(lst, x)
        sumatoriaCount = sumatoria + float(movie["vote_count"])
        sumatoriaAverage = sumatoria + float(movie["vote_average"])
        counter = counter + 1
        print(movie["title"])
    promedioCount = sumatoriaCount/counter
    promedioAverage = sumatoriaAverage/counter
    if i == 1:
        print("Promedio de votos del ranking: "+str(round(promedioCount,1)))
        print("Promedio de calificación del ranking: "+str(round(promedioAverage,1)))

def topBestAverage (lst, numero, i): #Vote_Average
    shell.shellSort(lst, compareAverageBest)
    sumatoria = 0
    counter = 0
    for x in range(0+i, numero):
        movie = lt.getElement(lst, x)
        sumatoriaCount = sumatoria + float(movie["vote_count"])
        sumatoriaAverage = sumatoria + float(movie["vote_average"])
        counter = counter + 1
        print(movie["title"])
    promedioCount = sumatoriaCount/counter
    promedioAverage = sumatoriaAverage/counter
    if i == 1:
        print("Promedio de votos del ranking: "+str(round(promedioCount,1)))
        print("Promedio de calificación del ranking: "+str(round(promedioAverage,1)))

def topWorstAverage (lst, numero, i): #Vote_Average
    shell.shellSort(lst, compareAverageWorst)
    sumatoria = 0
    counter = 0
    for x in range(0+i, numero):
        movie = lt.getElement(lst, x)
        sumatoriaCount = sumatoria + float(movie["vote_count"])
        sumatoriaAverage = sumatoria + float(movie["vote_average"])
        counter = counter + 1
        print(movie["title"])
    promedioCount = sumatoriaCount/counter
    promedioAverage = sumatoriaAverage/counter
    if i == 1:
        print("Promedio de votos del ranking: "+str(round(promedioCount,1)))
        print("Promedio de calificación del ranking: "+str(round(promedioAverage,1)))
 
#Requerimientos
def createRanking (lst, numero, criterio, orden):
    if criterio == 1:
        if orden == 1:
            topBestCount(lst, numero,0)
        elif orden == 2:
            topWorstCount(lst, numero,0)
        else: print("El valor ingresado no es válido")
    elif criterio == 2:
        if orden == 1:
            topBestAverage(lst, numero,0)
        elif orden == 2:
            topWorstAverage(lst, numero,0)
        else: print("El valor ingresado no es válido")
    else: print("El valor ingresado no es válido")

def directorInfo (directorsList, detailsList, nombre):
    nombre = nombre.title()
    sumatoria = 0
    if lt.isPresent(directorsList, nombre):
        directorPos = lt.isPresent(directorsList, nombre)
        director = lt.getElement(directorsList, directorPos)
        iterator = it.newIterator(director["movies"])
        print("\nPelículas dirigidas por "+nombre+":\n")
        while(it.hasNext(iterator)):
            movieNumber = it.next(iterator)
            moviePos = lt.isPresent(detailsList, movieNumber)
            movieDetails = lt.getElement(detailsList, moviePos)
            sumatoria = sumatoria + float(movieDetails["vote_average"]) 
            print(movieDetails["title"])
        size = lt.size(director["movies"])
        promedio = sumatoria/size
        print("\nCantidad de películas: " + str(size))
        print("Promedio de calificación de películas: "+str(round(promedio,1)))
    else: print("El nombre ingresado no está disponible")
 
def actorInfo (lstActors,detailsList,nombre, directorsList):
    nombre = nombre.title()
    sumatoria = 0
    if lt.isPresent(lstActors, nombre):
        actorPos = lt.isPresent(lstActors, nombre)
        actor = lt.getElement(lstActors, actorPos)
        iterator = it.newIterator(actor["movies_id"])
        print("\nPelículas donde actua "+nombre+":\n")
        while(it.hasNext(iterator)):
            movieNumber = it.next(iterator)
            moviePos = lt.isPresent(detailsList, movieNumber)
            movieDetails = lt.getElement(detailsList, moviePos)
            sumatoria = sumatoria + float(movieDetails["vote_average"]) 
            print(movieDetails["title"])
        colab = {i:actor["colabs"].count(i) for i in actor["colabs"]}
        colab = max(colab, key=colab.get)
        print ("\nEl director con mas colaboraciones es: " + colab)
        size = lt.size(actor["movies_id"])
        promedio = sumatoria/size
        print("\nCantidad de películas: " + str(size))
        print("Promedio de calificación de películas: "+str(round(promedio,1)))
    else: print("El nombre ingresado no está disponible")
 
def genreInfo (lstGenres,detailsList,nombre):
    nombre = nombre.title()
    sumatoria = 0
    if lt.isPresent(lstGenres, nombre):
        genrePos = lt.isPresent(lstGenres, nombre)
        genre = lt.getElement(lstGenres, genrePos)
        iterator = it.newIterator(genre["lstMovies"])
        print("\nPelículas del genero "+nombre+":\n")
        while(it.hasNext(iterator)):
            movieNumber = it.next(iterator)
            moviePos = lt.isPresent(detailsList, movieNumber)
            movieDetails = lt.getElement(detailsList, moviePos)
            sumatoria = sumatoria + float(movieDetails["vote_average"]) 
            print(movieDetails["title"])
        size = lt.size(genre["lstMovies"])
        promedio = sumatoria/size
        print("\nCantidad de películas: " + str(size))
        print("Promedio de calificación de películas: "+str(round(promedio,1)))
    else: print("El género ingresado no está disponible")

def getMoviesByGenre(lstGenres, detailsList, genero):
    genero = genero.title()
    listaDelGenero = lt.newList()
    counter = 0
    if lt.isPresent(lstGenres, genero):
        genrePos = lt.isPresent(lstGenres, genero)
        genre = lt.getElement(lstGenres, genrePos)
        iterator = it.newIterator(genre["lstMovies"])
        while(it.hasNext(iterator)):
            movieNumber = it.next(iterator)
            moviePos = lt.isPresent(detailsList, movieNumber)
            movieDetails = lt.getElement(detailsList, moviePos)
            lt.addFirst(listaDelGenero, movieDetails)
            counter +=1
    else: print("El género ingresado no está disponible")
    return listaDelGenero
    
def createGenreRanking (genreLst, numero, criterio, orden):
    if criterio == 1:
        if orden == 1:
            topBestCount(genreLst, numero+1,1)
        elif orden == 2:
            topWorstCount(genreLst, numero+1,1)
        else: print("El valor ingresado no es válido")
    elif criterio == 2:
        if orden == 1:
            topBestAverage(genreLst, numero+1,1)
        elif orden == 2:
            topWorstAverage(genreLst, numero+1,1)
        else: print("El valor ingresado no es válido")
    else: print("El valor ingresado no es válido")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados
    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
 
 
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            
            if int(inputs[0])==1: #opcion 1
                lstDetails = loadMoviesDetails()
                lstCasting = loadMoviesCasting()
                lstDirectors = loadDirectors()
                lstActors = loadActors()
                lstGenres = loadGenres()
            elif int(inputs[0])==2: #opcion 2
                numero = input("Ingrese el número de películas en el ranking o presione enter para valor por defecto (10): ")
                criterio = int(input("Ingrese el criterio deseado para el ranking: \n1.Vote Count  2.Vote Average\n"))
                orden = int(input("Ingrese el tipo de orden que desea en su ranking: \n1.Top Best  2.Top Worst\n"))
                if numero == "":
                    numero = 10
                else: numero = int(numero)
                createRanking(lstDetails, numero, criterio, orden)
                pass
 
            elif int(inputs[0])==3: #opcion 3
                nombre = input("Ingrese el nombre del director deseado: ")
                directorInfo(lstDirectors, lstDetails, nombre)
                pass
 
            elif int(inputs[0])==4: #opcion 4
                nombre = input("Ingrese el nombre del actor deseado: ")
                actorInfo(lstActors, lstDetails, nombre, lstDirectors)
                pass
 
            elif int(inputs[0])==5: #opcion 5
                nombre = input("Ingrese el nombre del genero deseado: ")
                genreInfo(lstGenres, lstDetails, nombre)
                pass

            elif int(inputs[0])==6: #opcion 6
                nombre = input("Ingrese el nombre del genero deseado: ")
                numero = input("Ingrese el número de películas en el ranking o presione enter para valor por defecto (10): ")
                criterio = int(input("Ingrese el criterio deseado para el ranking: \n1.Vote Count  2.Vote Average\n"))
                orden = int(input("Ingrese el tipo de orden que desea en su ranking: \n1.Top Best  2.Top Worst\n"))
                if numero == "":
                    numero = 10
                else: numero = int(numero)
                genreLst = getMoviesByGenre(lstGenres, lstDetails, nombre)
                createGenreRanking(genreLst, numero, criterio, orden)
                pass
 
 
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
