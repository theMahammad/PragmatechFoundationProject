# Ən kiçik elementi tapmaq
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def findMin(list):
    list.sort()
    
    return list[0]
print(findMin(myList))