# Tək indekslilərin silinməsi
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def removeOddIndexes(list):
      newList = []
      for index, item in enumerate(list):
          
          if(index%2==0):
              newList.append(item)
      print(newList)
removeOddIndexes(myList)  