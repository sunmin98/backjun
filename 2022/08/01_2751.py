import sys
a = int(sys.stdin.readline())

def counting(arr):
    m = max(lists)
    C = [0] * (m + 1)
    for a in arr:
        C[a] += 1
    for i in range(1, m + 1):
        C[i] += C[i - 1]
    result = [0] * len(arr)
    for a in arr:
        result[C[a] - 1] = a
        C[a] -= 1
    return result

lists = []

for i in range(0,a):
    lists.append(int(sys.stdin.readline()))

lists = counting(lists)

for i in lists:
    print(i)