def solution(lists, num):
	RT_list = [0]
	CF_list = [0]
	JM_list = [0]
	AN_list = [0]

	for i in range(len(lists)):
		if lists[i] == "AN":
			AN_list.append(num[i] - 4)
		elif lists[i] == "NA":
			AN_list.append(4 - num[i])

		elif lists[i] == "JM":
			JM_list.append(num[i] - 4)
		elif lists[i] == "MJ":
			JM_list.append(4 - num[i])

		elif lists[i] == "RT":
			RT_list.append(num[i] - 4)
		elif lists[i] == "TR":
			RT_list.append(4 - num[i])

		elif lists[i] == "CF":
			CF_list.append(num[i] - 4)
		elif lists[i] == "FC":
			CF_list.append(4 - num[i])

	RT_list = sum(RT_list)
	CF_list = sum(CF_list)
	JM_list = sum(JM_list)
	AN_list = sum(AN_list)
	print(RT_list, CF_list, JM_list, AN_list)

	# 최종 결과 문자열 생성
	result = ""
	if RT_list <= 0:
		result += "R"
	else:
		result += "T"

	if CF_list <= 0:
		result += "C"
	else:
		result += "F"

	if JM_list <= 0:
		result += "J"
	else:
		result += "M"

	if AN_list <= 0:
		result += "A"
	else:
		result += "N"

	return result


# 예시 테스트
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3]))  # "RCJA"
