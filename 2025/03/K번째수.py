def solution(array, commands):
	answer = []

	for num in range(len(commands)):
		i = commands[num][0] - 1
		j = commands[num][1]
		kk = commands[num][2] -1
		lists = []

		for k in range(i, j):
			lists.append(array[k])

		# print(i, j)
		# print(lists)
		lists.sort()
		# print(lists)
		# print(kk)
		answer.append(lists[kk])

	return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
