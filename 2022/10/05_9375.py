import math

a = int(input())

for i in range(a):
    b = int(input())
    lists = []
    lists_fin = []
    for j in range(b):
        num1, num2 = map(str, input().split())
        lists.append(num2)
    lists_set = set(lists)

    for i in lists_set:
        lists_fin.append(lists.count(i)+1)

    print(math.prod(lists_fin)-1)
