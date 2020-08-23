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
    

