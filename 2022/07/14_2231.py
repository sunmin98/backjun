a = int(input())
length = len(str(a))
ans_lists = []
lists = []
num = 0
for i in range(1, a):

	lists.append(i)
	for j in range(length - 1, -1, -1):
		lists.append(i // (10 ** j))
		i -= (i // (10 ** j)) * (10 ** j)
	# print(sum(lists))
	if a == sum(lists):
		# print("띵똥",lists)
		ans_lists.append(lists[0])
	lists = []

if len(ans_lists) == 0 :
	print('0')
else: print(min(ans_lists))
