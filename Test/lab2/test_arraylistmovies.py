def newlist(cmpfunction, list_name):
    """
    Crea una array list vacia

    arg:
        -cmpfunction: Funcion de comparacion entre los elementos.
        -list_name: Nombre que desea asignarle a la lista.
    """
    list_name = {'elements':[], 'size':0, 'type':'ARRAY_LIST', 'cmpfunction':cmpfunction}
    return list_name

def addfirst(element,lst):
    """
    Agrega un elemento al inicio de la lista.

    arg:
        -element: El elemento que se desea agregar. 
    
    raise:
        -No se pudo a gregar el elemento.
    """
    try:
        lst['elements'].insert(0,element)
        lst['size']+=1
    except:
        raise Exception('No se pudo agregar el elemento. Por favor verifique la lista')

def addLast(element,lst):
    """
    Agrega un elemento al final de la lista.

    arg:
        -element: El elemento que se desea agregar
        -lst: La lista que se desea modificar
    
    raise:
        -No se pudo agregar el elemento.
    """
    try:
        lst['elements'].insert(0,element)
        lst['size']+=1
    except:
        raise Exception('No se pudo agrgar el elemento. Por favor verifique la lista')

def isEmpty(lst):
    """
    Determina sí una lista esta vacia o no.

    arg:
        -lst: La lista de la cual se desea saber esa informacion.
    
    raise:
        -Existe un problema con la lista.
    """
    try:
        return lst['size'] == 0
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def size(lst):
    """
    Determina la longitud de la lista.

    arg:
        -lst: La lista de la cual se desa saber su longitud.

    raise:
        -Existe un problema con la lista.
    """
    try:
        return lst['size']
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def firstElement(lst):
    """
    Retorna el primer elemento de la lista.

    arg: 
        -lst: La lista de la cual se desea conocer su primer elemento.
    
    raise:
        -Existe un problema con la lista.
    """
    try:
        return lst['elements'][0]
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def lastElement(lst):
    """
    Retorna el ultimo elemento de la lista.

    arg:
        -lst: La lista de la cual se desea saber su ultimo elemento.
    
    raise:
        -Existe un problema con la lista
    """
    try:
        return lst['elements'][lst['size']-1]
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def getElement(pos, lst):
    """
    Retorna el elemento de la posicion indicada

    arg:
        -lst: La lista de la cual se desea conocer el elemento
        -pos: Posicion que se desea conocer

    Raise:
        -Problema con la lista o la posicion
    """
    try:
        return lst['elements'][pos-1]
    except:
        if pos not in range(0,lst['size']+1):
            raise Exception('La longitud de la lsita es menor que la posicion pasada por parametro')
        else:
            raise Exception('Existe un problema con la lista. Verifique la lista')

def deleteElement(pos, lst)
"""
Elimina el eleemnto de la posicion indicada.

arg:
    -lst: Lista en la cual se desea remover un elemento.
    -pos: posicion del elemento el cual se desea eliminar.

Raises:
    -Problema con la lista o la posicion.
"""
try:
    lst['elements'].pop(pos-1)
    lst['size']-=1
except:
    if pos not in range(0,lst['size']+1):
        raise Exception('La posicion pasada por parametro es mayor que la longitud de la lista')
    else:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def removeFirst(lst):
    """
    Elimina el primer elemento de una lista.
    arg:
        -lst: La lista de la cual se desea eliminar el primer elemento.
    
    Raises:
        -problema con la lista
    """
    try:
        lst['elements'].pop(0)
        lst['size']-=1
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def removeLast(lst):
    """
    Elimina el ultimo elemento.
    arg:
        -lst: La lista de la cual se desea eliminar el ultimo elemento.
    
    Raises:
        -problema con la lista
    """
    try:
        lst['elements'].pop(lst['size']-1)
        lst['size']-=1
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def insertElement(element, pos, lst):
    """
    Inserta un elemento en la posicion indicada.
    arg:
        -element: Elemento que se desea insertar.
        -pos: Posicion en la cual se desea insertar.
        -lst: Lista en la cual se desea insertar el elemento.
    Raises:
        -problema con la lista.
    """
    try:
        lst['elements'].insert(pos-1, element)
        lst['size']+=1
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def isPresent(element, lst):
    """
    Determina sí un elemento esta presente en la lista
    arg:
        -element: El elemento que se desea buscar.
        -lst: La lista que se esta examinando.
    Raises:
        -problema con la lista
    """
    try:
        top=lst['size']
        exist=False
        if top > 0:
            i=0
            while i < top and not exist:
                if (lst['cmpfunction'](element,lst['elements'][i])):
                    exist=True
        return exist
    except:
        raise Exception('Existe un problema con la lista. Verifique la lista')

def changeInfo(pos, newinfo, lst):
    """
    Cambia la informacion de un elmento.
    arg:
        -pos: Posicion del elemeneto del que se desa actualizar la informacion.
        -newinfo: Informacion actualizada.
        -lst: Lista sobre la que se hace el proceso.

    Raises:
        -Problema con la lista.
        -Problema con las posiciones pasadas por parametro.
    """
    try:
        lst['elments'][pos-1]=newinfo
    except:
        if pos not in range(0,lst['size']+1):
            raise Exception('La posicion no se encuentra en el rango de la longitud de la lista')
        else:
            raise Exception('Existe un problema con la lista. Verifique la lista')

def exchange(pos1, pos2, lst):
    """
    Cambia la posicion de dos elementos.
    arg:
        -pos1: Posicion del primer elemento.
        -pos2: Posicion del segundo elemento.
        -lst: Lista sobre la cual se haced el intercambio.
    Raises:
        -Problema con la lista.
        -Problema con las posiciones pasadas por parametro.
    """
    try:
        element1=lst['elements'][pos1-1]
        element2=lst['elements'][pos2-1]
        changeInfo(pos1, element2, lst)
        changeInfo(pos2, element2, lst)
        return lst
    except:
        if pos1 not in range(0,lst['size']+1) or pos2 not in range(0,lst['size']+1):
            raise Exception('Una de las posiciones se sale de el rango de la lista')
        else:
            raise Exception('Existe un problema con la lista. Verifique la lista')

def subList(size, pos, lst):
    """
    Se retorna una lista la cual inicia en la posicion dada y termina en la longitud de elementos.
    arg:
        -size: La longitud de la lista.
        -pos: Posicio desde la cual se desea crear la sublista.
        -lst: Lista sobre la cual se hace el proceso.

    Raises:
        -Posicion fuera de lista.
        -Problema con la lista.
    """
    try:
        subList=newlist(lst['cmpfunction'], 'sublista')
        element=pos-1
        i=1


