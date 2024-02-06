n, k = map(int, input().split())
n += 1
lists = [[0 for j in range(n)] for i in range(k)]

for i in range(k):
	lists[i][0] = 1
	for i in range(k):
		lists[i][0] = 1
for i in range(n):
	lists[0][i] = 1

for i in range(1, k):
	for j in range(n):
		lists[i][j] = lists[i - 1][j] + lists[i][j - 1]

# print(lists)
print(lists[-1][-1]%1000000000)
