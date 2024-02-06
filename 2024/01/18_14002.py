num = int(input())

lists = list(map(int, input().split()))
dp = [0] * num

for i in range(num):
	if dp[i] == 0:
		dp[i] = 1
	for j in range(i):
		if lists[i] > lists[j]:
			dp[i] = max(dp[i], dp[j] + 1)
max_ans = max(dp)

print(max_ans)
# print(dp)

lists4 = [list(t) for t in zip(lists, dp)]
lists3 = [list(t) for t in zip(lists, dp)].reverse()
reversed_list = lists4[::-1]

# print(lists4)
# print(reversed_list)
ans_list = []

for i in range(0, num):
	for j in range(0, num):
		if reversed_list[j][1] == max_ans:
			ans_list.append(reversed_list[j][0])
			max_ans -= 1
print(*reversed(ans_list))


# 13
# 3 4 5 6 2 3 1 7 4 3 5 6 7
