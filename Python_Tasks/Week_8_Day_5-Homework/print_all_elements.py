# Elementləri çap etmək 
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def printAllElement(list):

    for index, item in enumerate(list):
       
        print(f'{index}.element : {item}')
printAllElement(myList)