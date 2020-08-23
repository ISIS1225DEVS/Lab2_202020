def insertionSort(nlist)->list:
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue
   return nlist

nlist = [14,46,43,27,57,41,45,21,70]
print(nlist)
new=[]
new=insertionSort(nlist)
print (new)

