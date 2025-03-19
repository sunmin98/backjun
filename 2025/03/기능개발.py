import math


def solution(progresses, speeds):
	answer = []
	lists = []
	num = 1

	for i, j in zip(progresses, speeds):
		x = (100 - i) / j
		lists.append(math.ceil(x))
	# print(lists)

	i = 0
	while i < len(lists):
		num = 1
		for j in range(i + 1, len(lists)):
			if lists[i] < lists[j]:
				break
			else:
				num += 1
		answer.append(num)

		i += num


	return answer

print(solution([10, 30, 10], [1, 1, 1]))
print(solution([95, 96, 97], [1, 1, 1]))  # 예상 출력: [3]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([93, 30, 55], [1, 30, 5]))