a, b = map(int, input().split())
lists = []
ans = 0  # 제출
num = 0  # 더해지는거
num_b = b
for i in range(a):
	lists.append(int(input()))
len_lists = len(lists) - 1
# print(lists[len_lists])
count = 0
while True:
	if num_b < lists[len_lists]:
		len_lists -= 1
	else:
		count = num_b // lists[len_lists]
		num += lists[len_lists] *count
		ans += count
		num_b -= lists[len_lists] *count

	# print(num_b, num, count, lists[len_lists])
	if num_b == 0: break

print(ans)
