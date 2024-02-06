ans_lists = []

for i in range(int(input())):
	num = str(input())
	setting = []
	# 리스트 세팅
	for j in num:
		setting.append(j)

	# print("~~~~~\n")

	for _ in range(len(setting)):
		for k in range(1,len(setting)):
			if setting[0] == '(' and setting[k] == ')':
				setting.pop(k)
				setting.pop(0)
				break



	if len(setting) > 0:
		ans_lists.append('NO')
	elif len(setting) == 0:
		ans_lists.append('YES')
	# print(setting)

for i in ans_lists:
	print(i)
