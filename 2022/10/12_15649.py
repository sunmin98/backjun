N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:  # 배열의 길이를 확인
        return print(" ".join(map(str, ans)))  # 1 2 3 이런 상태로 출력하기 위해

    for i in range(1, N + 1):  # 1 ~ N 까지
        if i not in ans:  # 중복 확인
            ans.append(i)  # 배열 추가
            print(ans)
            back()  # 재귀
            ans.pop()  # return으로 돌아오면 이게 실행됨. 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것

back()

# def back():
#     if len(ans) ==M :
#         print(" ".join(map(str,ans)))
#         return
#
#     for i in range(1, N+1):
#         if i not in ans :
#             ans.append(i)
#             print(ans)
#             back()
#             ans.pop()


