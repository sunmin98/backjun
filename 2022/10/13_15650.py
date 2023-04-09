from itertools import combinations, permutations

a, b = map(int, input().split())

arr = []

for i in range(1, a + 1):
    arr.append(i)
lists = list(permutations(arr, b))


for i in range(len(lists)):
    for k in lists[i]:
        print(k ,end=' ')
    print()
