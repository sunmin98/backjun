num = int(input())
ans = []
list10 = [0, 1]
lists = []


def func(num):
	for i in range(0, num - 1):
		lists.append(list10[1 - i])
		if lists[-1] == 0:
			lists.append(0)
			if len(lists) >= num:
				return ans.pop(-1)

	return ans.append(lists)


func(num)
print(ans)
