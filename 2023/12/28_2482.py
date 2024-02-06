N = int(input())
K = int(input())

lists = [[0] * (1001) for _ in range(1001)]
lists[4][1] = 4
lists[4][2] = 2
lists[5][1] = 5
lists[5][2] = 5

for i in range(6, N + 1):
	lists[i][1] = i

# print(lists)

for i in range(6, N + 1):
	for j in range(2, K+1):
		lists[i][j] = (lists[i - 2][j - 1] + lists[i - 1][j]) % 1000000003

print(lists[N][K])
# print(lists)