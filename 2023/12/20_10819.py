import itertools

num = int(input())
lists = list(map(int, input().split()))

lists_1 = []

test = itertools.permutations(lists, num)
lists = list(test)

for i in range(0, len(lists)):
	ans = 0
	for j in range(0, num - 1):
		if j == num: break

		ans += abs(lists[i][j] - lists[i][j + 1])
	lists_1.append(ans)

print(max(lists_1))

# 6
# 20 1 15 8 4 10