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

def lessfunction (elemento1, elemento2):
    if elemento1<elemento2:
      return True
    return False


def insertionSort (lst, orden:str)->list: 
    print ("ahora si stoy aqui, voy a imprimir dos registros")
    print (lst[0])
    input ("clic para continuar")
    print (lst[1])
    input ("clic para continuar")
    size =  len(lst)-1 
    pos1 = 1
    
    # while pos1 <= size:
    #    pos2 = pos1
    #    while (pos2 >1) and (lessfunction (lst[pos2]['vote_count'], pos2),lst [pos2-1]['vote_count']):
    #        pivot=lst[pos2]
    #       lst[pos2]=lst [pos2-1]
    #        lst [pos2-1]=pivot
    #       pos2 -= 1
    #    pos1 += 1
    #   while (pos2 >1) and (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, pos2-1))):
    #            lt.exchange (lst, pos2, pos2-1)
    #           pos2 -= 1
    #       pos1 += 1
    
    for index in range(1,len(lst)):
     currentvalue = int(lst[index]['vote_count'])
     posM=int(currentvalue)
     position = index
     #print (currentvalue, " " , index , "  ", position)
     #input ("clic para avanzaar")
     while position>0 and int(lst [position-1]['vote_count'])>int(currentvalue):
         lst [position]=lst [position-1]
         position = position-1
         #print (currentvalue)
     #lst[position]['vote_count']=currentvalue
     print ("fuera de while",currentvalue)
     #input ("clic")
     #lst [position]=lst [position-1]
    input ("************************* dar clic para imprimir lista ordenada  en Insertion procedure  ********************")
    for i  in range (0,20,1):
      print (lst[i])
    
    return lst
