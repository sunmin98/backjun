lists = []
for _ in range(5):
	lists.append(int(input()))

print(int(sum(lists)/5))
lists_1 = sorted(lists)
print(lists_1[2])
