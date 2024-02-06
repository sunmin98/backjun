num = int(input())

if num < 4:
	lists_1 = [1, 3, 5]
	print(lists_1[num - 1] % 10007)
	quit()

lists = [0] * (num + 1)

lists[0] = 0
lists[1] = 1
lists[2] = 3
lists[3] = 5

for i in range(4, num + 1):
	lists[i] = 2 * (lists[i - 2]) + lists[i - 1]
	lists[i - 3] = 0

print(lists[num] % 10007)
