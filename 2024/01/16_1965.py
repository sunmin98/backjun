num = int(input())

lists = list(map(int, input().split()))
dp = [0] * num

for i in range(num):
	if dp[i] == 0:
		dp[i] = 1
	for j in range(i):
		if lists[i] > lists[j]:
			dp[i] = max(dp[i], dp[j] + 1)

		print(dp)

print(dp)
print(max(dp))