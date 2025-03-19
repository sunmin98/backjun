def solution(genres, plays):
	length = len(genres)
	dicts = {}
	sum_dicts = {}
	sample_list = []

	# (1) 재생횟수와 곡 인덱스를 함께 저장
	for i in range(length):
		if genres[i] not in dicts:
			dicts[genres[i]] = []
		dicts[genres[i]].append((plays[i], i))

	print(dicts)
	# (2) 장르별로 재생횟수 기준 오름차순 정렬 (원래 sort()도 오름차순이었으니 유지)
	for g in dicts:
		dicts[g].sort(key=lambda x: x[0])

	print(dicts)
	# (3) 장르별 합계 계산 (재생횟수만 합산)
	for g in dicts:
		sum_dicts[g] = sum(x[0] for x in dicts[g])

	print(sum_dicts)
	# (4) 장르 합계를 내림차순 정렬
	sum_dicts = sorted(sum_dicts.items(), key=lambda x: x[1], reverse=True)
	print(sum_dicts)

	# (5) 각 장르에서 '가장 큰 재생 횟수' 2곡 (뒤에서 2개) 추출
	for i in range(len(sum_dicts)):
		lists = dicts[sum_dicts[i][0]]  # [(플레이수, 인덱스), ...]

		if len(lists) == 1:
			# 곡이 하나뿐이라면 하나만
			sample_list.append(lists[-1])
		else:
			# 곡이 2개 이상이면 뒤에서 2개
			sample_list.append(lists[-1])
			sample_list.append(lists[-2])

	# (6) sample_list에는 (재생횟수, 인덱스) 형태가 들어있으므로
	#     인덱스만 모아서 결과를 만든다
	answer = []
	for item in sample_list:
		# item은 (재생횟수, 인덱스) 튜플
		answer.append(item[1])

	return answer


# 테스트
print(solution(["classic", "pop", "classic", "classic", "pop"],
			   [500, 600, 150, 800, 2500]))
