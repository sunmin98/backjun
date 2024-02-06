num = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 촌수 계산해야 하는 사람 번호
m = int(input())  # 부모 자식 관계 갯수
ans = 0

lists = [[] for _ in range(num + 1)]

for _ in range(m):
	s, e = map(int, input().split())
	lists[s].append(e)
	lists[e].append(s)

for i in range(1, num + 1):
	lists[i].sort()

ans_dfs = []
ans_bfs = []
v = [0] * (num + 1)


# def dfs(c):
# 	ans_dfs.append(c)  # 방문 노드 추가
# 	v[c] += v[c] + 1  # 방문 표시
# 	for n in lists[c]:
# 		if not v[n]:  # 방문하지 않은 노드인 경우
# 			dfs(n)


def bfs(s):
	q = []  # 필요한 q, v[], 변수 생성

	q.append(s)  # Q에 초기데이터(들) 삽입
	ans_bfs.append(s)
	v[s] = 1

	while q:
		c = q.pop(0)

		if c == b:
			return

		for n in lists[c]:
			if not v[n]:  # 방문하지 않은 노드=>큐 삽입
				q.append(n)
				ans_bfs.append(n)
				v[n] += v[c] + 1


bfs(a)
# dfs(a)
# print(ans_bfs)
# print(v)
# print(ans_dfs)

if b not in ans_bfs:
	print(-1)
else:
	print(v[b] - 1)
