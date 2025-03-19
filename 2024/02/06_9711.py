num = int(input())
dp = [0] * 10001

dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3
dp[5] = 5

for i in range(6, 10001):
	dp[i] = (dp[i - 1] + dp[i - 2])

# print(dp[:10])
for j in range(1, num + 1):
	a, b = map(int, input().split())
	print("Case #{0}: {1} ".format(j, dp[a] % b))