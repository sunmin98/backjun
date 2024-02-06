com_num = int(input())
com_couple = int(input())
lists = [[] for _ in range(com_num + 1)]

for _ in range(com_couple):
	s, e = map(int, input().split())
	lists[s].append(e)
	lists[e].append(s)  # 양방향

# [1] 오름차순 정렬
for i in range(1, com_num + 1):
	lists[i].sort()

# print(lists)

ans_dfs = []
v = [0] * (com_num + 1)


def dfs(c):
	ans_dfs.append(c)  # 방문 노드 추가
	v[c] = 1  # 방문 표시
	for n in lists[c]:
		if not v[n]:  # 방문하지 않은 노드인 경우
			dfs(n)


dfs(1)
print(len(ans_dfs)-1)
