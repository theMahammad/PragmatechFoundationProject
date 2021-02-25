# 3 ədəddən ən böyüyünü tapan funksiya
def maxOfThree(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(f'3 ədəddən ən böyüyü :  {maxOfThree(5,67,56)}')
# İstənilən sayda ədəddən ən böyüyünü tapan funksiya
def maxElement(*args):
    max = args[0] 
    for arg in args:
        if arg>max:
            max = arg
    return max

print(f'İstənilən sayda  ədəddən ən böyüyü :  {maxElement(5,67,2,3,89,23)}')


        

