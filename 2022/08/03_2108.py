#import numpy
from collections import Counter

a = int(input())
lists = []
lists_sort=[]
arr=[0] * 4000

for i in range(0,a):
    lists.append(int(input()))

lists_sort = sorted(lists)

print(round(sum(lists_sort))/len(lists_sort)) #산술평균

print(int(numpy.median(lists_sort))) #중앙값

# 최빈값.
mode=Counter(lists_sort).most_common(1)
#print(mode[0][0])
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

if lists_sort[0]-lists_sort[len(lists_sort)-1] <0 :
    print((lists_sort[0]-lists_sort[len(lists_sort)-1])*-1)
else : print(lists_sort[0]-lists_sort[len(lists_sort)-1]) #범위