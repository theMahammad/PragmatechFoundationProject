myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
# Cüt yerdə duran elementlərin tapılması
def printEvenIndexes(list):
     for index, item in enumerate(myList):
         if index%2==0:
             print(item)
printEvenIndexes(myList)