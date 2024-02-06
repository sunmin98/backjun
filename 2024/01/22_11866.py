a, b = map(int, input().split())
num = 0
lists = []
ans = []
for i in range(1, a + 1):
	lists.append(i)

for i in range( a):
	num += b-1

	if num >= len(lists):
		num = num % len(lists)
	ans.append(lists.pop(num))

print(str(ans).replace('[', '<').replace(']', '>'))


