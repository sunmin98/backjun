A = int(input())
ANS = 0
NUM = str(input())
lists = []
for i in range(1, A):
	lists.append(input())

	if lists[-1] == 'ENTER':
		ANS += len(set(lists)) - 1
		lists = []
ANS += len(set(lists))
print(ANS)
