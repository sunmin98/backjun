a, b = map(int, input().split())

lists = list(map(int, input().split()))
ans_lists = []

for i in lists:
	if b > i:
		ans_lists.append(i)
print(*ans_lists)
