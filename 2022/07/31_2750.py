a = int(input())
lists = []
lists_sort=[]

for i in range(0,a):
    lists.append(int(input()))

lists_sort = sorted(lists)

for i in lists_sort:
    print(i)