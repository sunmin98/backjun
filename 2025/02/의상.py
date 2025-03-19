def solution(clothes):
	dict_clothes = dict(clothes)
	answer = 1
	# 딕셔너리로 개수 세기
	count_dict = {}
	for item in list(dict_clothes.values()):
		if item in count_dict:
			count_dict[item] += 1
		else:
			count_dict[item] = 1

	# print(count_dict)

	for key, value in count_dict.items():
		# print(key, value)
		answer *= value+1

	return answer-1


print(solution([['a', '1'], ['b', '1'], ['c', '2'], ['d', '2'],
				['e', '3'], ['f', '3'], ['g', '4'], ['h', '4']]))

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
				["green_turban", "headgear"]]))  # False가 나와야 하지만 True가 나옴
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
