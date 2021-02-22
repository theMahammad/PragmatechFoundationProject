# Elementlərin cəminin tapılması
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
def findSum(list):
    sum = 0
    for item in list:
        sum+=item
    return sum
print(findSum(myList))

