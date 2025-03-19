import sys

sys.setrecursionlimit(10 ** 6)

T = int(input())  # T번 반복


def DFS(x, y):
	if x < 0 or y < 0 or x >= M or y >= N:
		return False
	if lists[y][x] == 1:
		lists[y][x] = 0
		DFS(x - 1, y)
		DFS(x + 1, y)
		DFS(x, y + 1)
		DFS(x, y - 1)
		return True

	return False


for _ in range(T):  # T개 케이스
	M, N, K = map(int, input().split())  # M-가로 N-세로 K-배추겟수
	lists = []
	ans = 0
	for i in range(N):
		row = [0] * M
		lists.append(row)
	for _ in range(K):
		x, y = map(int, input().split())
		lists[y][x] = 1
	for i in range(N):
		for j in range(M):
			if lists[i][j] == 1:
				DFS(j, i)
				ans += 1  # 그룹 수 증가

	print(ans)