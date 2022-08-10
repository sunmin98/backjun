lists = []
list_num , cut = map(int, input().split())

lists = list(map(int, input().split()))


#print(list)

list_sort=sorted(lists, reverse=True)

#print(list_sort)

print(list_sort[cut-1])

