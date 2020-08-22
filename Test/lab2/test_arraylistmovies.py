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
        raise Exception("No se pudo agregar el elemento. Por favor verifique la lista")

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
        raise Exception("No se pudo agrgar el elemento. Por favor verifique la lista")

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
        raise Exception("Existe un problema con la lista. Verifique la lista")

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
        raise Exception("Existe un problema con la lista. Verifique la lista")

def firstElement(lst):
    """
    Retorna el primer elemento de la lista.

    arg: 
        -lst: La lista de la cual se desea conocer su primer elemento
    
    raise:
        -Existe un problema con la lista.
    """
    try:
        return lst['elements'][0]
    except:
        raise Exception("Existe un problema con la lista. Verifique la lista")

def fir