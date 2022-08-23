N=int(input())
arr=[]
lists=[]
for i in range(N):
    a = input()
    arr.append(a)

arr=set(arr)
arr=list(arr)

for i in range(len(arr)):
    lists.append((len(arr[i]),arr[i]))

lists.sort()

for i in range(len(lists)):
    print(lists[i][1])

