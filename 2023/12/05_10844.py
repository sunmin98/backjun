num = int(input())

dp = [[0 for _ in range(10)] for j in range(num)]

for i in range(1, 10):
	dp[0][i] = 1

for i in range(1, num):
	for j in range(0, 10):
		if j == 0:
			dp[i][j] += dp[i - 1][j + 1]
		elif j == 9:
			dp[i][j] += dp[i - 1][j - 1]
		else:
			dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[num - 1]) % 1000000000)
