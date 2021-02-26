# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Ikincini tapmaq
list = [5,6,7,8,8,5]

def findRunnerUp(list):
    list.sort()
    list.reverse()
    for i in list:
        if i<list[0]:
            print(i)
            break
findRunnerUp(list)

