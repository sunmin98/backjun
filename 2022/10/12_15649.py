# from itertools import combinations, permutations
#
# a, b = map(int, input().split())
#
# arr = []
#
# for i in range(1, a + 1):
#     arr.append(i)
# lists = list(permutations(arr, b))
#
#
# for i in range(len(lists)):
#     for k in lists[i]:
#         print(k ,end=' ')
#     print()


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        print(s)
        print(visited)
        visited[i] = False


n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

dfs()




