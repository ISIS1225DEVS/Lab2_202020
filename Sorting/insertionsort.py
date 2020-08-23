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

#less and greater fuction

def lessfunction(element1, element2, criteria):
    element1=element1[criteria]
    element2=element2[criteria]
<<<<<<< HEAD
    if element1 <= element2:
=======
    if element1[:3] <= element2[:3]:
>>>>>>> master
        return 1
    else:
        return 0

def greaterfunction(element1, element2, criteria):
    element1=element1[criteria]
    element2=element2[criteria]
    if element1 >= element2:
        return 1
    else:
        return 0

#funcion de ordenamiento

def insertionSort (lst, lessfunction, criteria): 
    size =  lt.size(lst) 
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 >1) and (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, pos2-1), criteria)):
            lt.exchange (lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
