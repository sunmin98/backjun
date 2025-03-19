def solution(arr):
	answer = []

	i = 0
	while True:
		try:
			if arr[i] == arr[i + 1]:
				arr[i]="q"
		except:
			break
		# print(arr, i)
		i += 1

	answer = list(filter(lambda x: x != "q", arr))
	# print(answer)

	return answer


print(solution(	[4, 4, 4, 3, 3]))
