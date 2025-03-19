from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))  # (인덱스, 우선순위) 형태로 저장
    answer = 0

    while queue:
        print(queue)
        cur = queue.popleft()  # 맨 앞 원소 가져옴
        print(cur)
        print(cur[0])
        print(cur[1])
        if any(cur[1] < x[1] for x in queue):  # 더 높은 우선순위가 존재하면
            queue.append(cur)  # 뒤로 보냄
        else:  # 실행될 경우
            answer += 1
            if cur[0] == location:  # 찾고자 하는 위치라면 종료
                return answer


print(solution([2, 1, 3, 2], 2))