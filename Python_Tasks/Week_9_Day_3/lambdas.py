# list = [5,6,26,3]
# def filterElements(expression):
#     for arg in list:
#         if expression(arg):
#             print(arg)
# filterElements(lambda x : x%2==0)
numbers = [3,56,78,12,56,25]


def filterElements(expression):
    for item in numbers:
        if expression(item):
            print(item)
# 5-ə bölünənlər
filterElements(lambda x :x%5==0)
# Rəqəmlər
filterElements(lambda x : x<10)
# Rəqəmlərinin cəmi 10-dan böyük olanlar
filterElements(
     lambda n: sum(int(d) for d in str(n))>10
    )


