num = str(input())

ans_num = len(num)
revers_num = num[::-1]
i = 0

# print(num[0])
for _ in range(len(revers_num)):
	if num == revers_num:
		break
	else:
		num = num[1:]
		revers_num = revers_num[:-1]
		i += 1

print(ans_num + i)
