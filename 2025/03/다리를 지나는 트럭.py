from collections import deque


def solution(bridge_length, weight, truck_weights):
	answer = 0  # 경과 시간
	bridge = deque()  # 다리 위의 트럭 (트럭 무게, 다리에서 보낸 시간)
	bridge_after = deque()  # 다리를 지난 트럭
	bridge_before = deque(truck_weights)  # 대기 트럭
	bridge_weight = 0  # 현재 다리 위 트럭의 총 무게

	while True:
		print(bridge_before, bridge, bridge_after)  # 디버깅 출력

		answer += 1  # 1초 경과

		# 다리를 지난 트럭을 bridge_after로 이동
		if bridge and bridge[0][1] == bridge_length:
			print(bridge[0][1])
			bridge_weight -= bridge.popleft()[0]
			bridge_after.append(1)  # 단순한 개수 저장

		# 새로운 트럭이 다리에 올라갈 수 있는지 확인
		if bridge_before and bridge_weight + bridge_before[0] <= weight and len(bridge) < bridge_length:
			truck = bridge_before.popleft()
			bridge.append((truck, 0))  # 다리 위로 올림 (트럭 무게, 경과 시간 0)
			bridge_weight += truck

		# 다리 위 트럭 이동
		bridge = deque((w, t + 1) for w, t in bridge)

		# 모든 트럭이 다리를 건넜으면 종료
		if len(bridge_after) == len(truck_weights):
			break

	return answer


print(solution(2, 10, [7, 4, 5, 6]))  # 8
