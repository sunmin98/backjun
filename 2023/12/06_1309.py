num = int(input())
num += 1
jump = 2
dp = [0] * num
dp[0] = 1
dp[1] = 3

for i in range(2, num):
	dp
	dp[i] = (2 * dp[i - 1] - dp[i - 2] + jump) % 9901
	jump = 2 * (jump + 1)

print(dp)
print(dp[num - 1] % 9901)
