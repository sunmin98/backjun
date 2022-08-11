a = int(input())
lists=[]
lists_s=[]

for i in range(0,a):
    lists = list(map(int, input().split()))
    lists_s.append(lists[0])

print(lists)
