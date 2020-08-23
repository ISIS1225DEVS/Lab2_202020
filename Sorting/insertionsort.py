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
   

    size =  len(lst)-1 
    pos1 = 1
    
    for i  in range (0,50,):
      print (lst[i])
     

    #input ("clic")


    
    for index in range(1,len(lst)):
     currentvalue = int(lst[index]['vote_count'])
     position = index
     original=lst[index]
     #print (currentvalue, " " , index , "  ", position)
     #input ("clic para avanzaar")
     while position>0 and int(lst [position-1]['vote_count'])>int(currentvalue):
         lst [position]=lst [position-1]
         position = position-1
         #print (currentvalue)
     lst[position]=original

    input ("************************* dar clic para imprimir lista ordenada  en Insertion procedure  ********************")

     
    if (orden == "a"):
          print ("Se ordeno ascendentemente")
          
    if (orden=="d"):
            for i  in range (0,len(lst)):
                tempo= lst[len(lst)]
                lst[len(lst)-i]=lst[i]
                lst[i]=tempo
            print ("Se ordeno descendentemente")

    for i  in range (0,len(lst),1):
          print (lst[i]['vote_count'])
    return lst
