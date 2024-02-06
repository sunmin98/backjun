num = int(input())

if num % 2 != 0:
	print(0)
	quit()

lists = [0] * 31
lists[2] = 3
lists[4] = 11
lists[6] = 41

for i in range(7, 31):
	if i % 2 != 0:
		lists[i] = 0
	else:
		lists[i] = (2 * sum(lists)) + lists[i - 2] + 2

# print(lists)
print(lists[num])
