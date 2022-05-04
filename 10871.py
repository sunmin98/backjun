a,b = map(int, input().split())

list = list(map(int, input().split()))

for i in range(list):
    if a>list[i] and b>list[i] :
        print(list[i], end=' ')