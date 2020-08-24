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
    
def insertionSort (lst, lessfunction, criteria): 
    size =  lt.size(lst) 
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 >1) and (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, pos2-1), criteria)):
            lt.exchange (lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
