a = int(input())

lists = []

for i in range(a):
    lists.append(list(map(int, input().split())))

print(lists)
