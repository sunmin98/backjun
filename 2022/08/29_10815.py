num_1 = int(input())
lists_1 = list(map(int, input().split()))

num_2 = int(input())
lists_2 = list(map(int, input().split()))

list = [False for i in range(20000000)]
for i in lists_1: list[i] = True

for i in lists_2:
    print([0,1][list[i]], end=' ')