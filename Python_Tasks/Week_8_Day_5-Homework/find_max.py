# Ən böyük elementi tapmaq
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
#  Built-in  metod
def findMax(list):
    list.sort()
    list.reverse()
    return list[0]
print(findMax(myList))
# Built-in olmayan metod
def findMax2(list):
    max = list[0]
    for item in list:
        if item>max:
            max=item
    return max
print(findMax2(myList))        