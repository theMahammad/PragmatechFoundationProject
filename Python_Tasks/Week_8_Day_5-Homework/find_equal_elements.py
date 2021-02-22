myList=[1,34,56,100,-12,87,987,1,3,5,56,67]



def findEqualElements(list):
    newList = []
    for item in list:
        if(list.count(item)>1):
            newList.append(item)
     # yeni massivde tekrar elementleri silmek 
    for item in newList:
        if newList.count(item)>1:
            newList.remove(item)
    return newList
         
print(findEqualElements(myList))




   
