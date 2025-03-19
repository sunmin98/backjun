from collections import deque


def Dfs(graph, v, visited):
	visited[v] = True
	print(v, end='')

	for i in graph[v]:
		if not visited[i]:
			Dfs(graph, i, visited)


def Bfs(graph, start, visited):
	queue = deque([start])

	visited[start] = True

	while queue:
		v = queue.popleft()
		print(v, end='')

		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

graph = [
    [],
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [3, 4],
]

visited = [False] * len(graph)

# print(visited)

Dfs(graph, 1, visited)
print("")
visited = [False] * len(graph)

Bfs(graph, 1, visited)
