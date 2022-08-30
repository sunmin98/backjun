import sys
input = sys.stdin.readline

N = int(input())
list_1 = [*map(int, input().split())]

M = int(input())
list_2 = [*map(int, input().split())]

count = {}
for i in list_1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

#print(count)

for i in list_2:
    if i in count:
        print(count[i],end=' ')
    else:
        print(0,end=' ')

