num = int((input()))

dp = [1] * 10

for i in range(2,num+1):
	for j in range(10):
		dp[j] = sum(dp[j:])

print(sum(dp)%10007)