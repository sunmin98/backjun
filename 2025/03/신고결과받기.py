def solution(id_list, report, k):
	report_lists = []  # 신고 당한애
	k_lists = []  # K개 이상인 애들
	k_dicts = {}
	report = set(report)
	for i in report:
		report_lists.append(i.split())

	for i in range(len(report_lists)):
		k_lists.append(report_lists[i][1])
	# print("report_lists->", report_lists)
	# print("k_lists->", k_lists)

	for i in k_lists:
		if i not in k_dicts:
			k_dicts[i] = 1
		else:
			k_dicts[i] += 1
	# print("k_dicts->", k_dicts)

	k_lists = []
	for key, value in k_dicts.items():
		if value >= k: k_lists.append(key)
	# print("k_lists->", k_lists)

	id_dicts = {string: 0 for string in id_list}


	for j in range(len(report_lists)):
		if report_lists[j][1] in k_lists:
			id_dicts[report_lists[j][0]] += 1
	# print(id_dicts)

	answer = list(id_dicts.values())
	return answer


print(
	solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
			 2))

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
