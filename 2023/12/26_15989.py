num = int((input()))

rows = 10001
lists = [0] * rows

lists[1] = 1
lists[2] = 2
lists[3] = 3
lists[4] = 4
lists[5] = 5
lists[6] = 7

for i in range(7, rows):
	lists[i] = 1 + (i // 2) + lists[i - 3]

for i in range(num):
	a = int((input()))
	print(lists[a])