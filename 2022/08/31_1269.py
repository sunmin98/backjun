a,b = map(int,input().split())
count=0
list_1 = [*map(int, input().split())]
list_1=set(list_1)

list_2 = [*map(int, input().split())]
list_2=set(list_2)

count+=len(list_1-list_2)
count+=len(list_2-list_1)

print(count)




