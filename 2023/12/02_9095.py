num1 = int(input())
ans = []
dp = [0] * 11
# print(dp)
dp[0] = 1
dp[1] = 2
dp[2] = 4
dp[3] = 7
for i in range(num1):
	num = int(input())
	if num <= 3:
		print(dp[num - 1])
		continue
	for i in range(4, num):
		# print(i)
		dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
	# print(dp)
	print(dp[num - 1])
