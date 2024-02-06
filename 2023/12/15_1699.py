N = int(input())

M = int(N ** 0.5)  # N의 제곱근(int변환)
dp = [n for n in range(N + 1)]

# print(M)
# print(dp)
# [1] 모든 값에 대해서 처리 => 소요시간: 284mS

# for i in range(2, M+1):
#     for j in range(1, N+1):
#         if j-i*i>=0:
#             dp[j]=min(dp[j], dp[j-i*i]+1)

# [2] 범위내의 값(업데이트 대상인 값만 처리) => 소요시간: 244mS
for i in range(2, M + 1):
	for j in range(i * i, N + 1):
		# print(dp[j - i * i] + 1)
		dp[j] = min(dp[j], dp[j - i * i] + 1)

# print(dp)
print(dp[N])