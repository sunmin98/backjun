def solution(participant, completion):
	participant_dict = {}

	# 한 번의 반복으로 딕셔너리 초기화 및 값 증가
	for i in participant:
		participant_dict[i] = participant_dict.get(i, 0) + 1

	# 도착자들 제외
	for i in completion:
		if i in participant_dict:
			participant_dict[i] -= 1

	for key in participant_dict:
		if participant_dict[key] > 0:
			return key

	return 0


# participant = []
# completion = []
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

solution(participant, completion)
