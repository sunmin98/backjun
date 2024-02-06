num = int(input())
lists = sorted(list(map(int, input().split())))
ans = 0

for i in lists:
	ans += i * num
	num -= 1

print(ans)
