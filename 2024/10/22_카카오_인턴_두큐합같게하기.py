
def solution(queue1, queue2):
	que_sum = sum(queue1) + sum(queue2)

	if que_sum % 2 != 0:
		return -1

	return 1


queue1 = [1,1]
queue2 = [1,5]

print(solution(queue1, queue2))
