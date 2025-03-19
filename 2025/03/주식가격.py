def solution(prices):
	answer = []
	lists = []
	length = len(prices)
	for i in range(len(prices)):
		lists.append(i)

	zip_lists = list(zip(lists, prices))

	for i in range(len(zip_lists)):
		flag = True

		for j in range(i + 1, len(zip_lists)):
			# print(zip_lists[i], zip_lists[j])
			if zip_lists[i][1] > zip_lists[j][1]:
				answer.append(zip_lists[j][0] - zip_lists[i][0])
				flag = False
				break

		if flag:
			answer.append(length - 1 - zip_lists[i][0])

		# print(answer)

	return answer


print(solution([1, 2, 3, 2, 3]))
