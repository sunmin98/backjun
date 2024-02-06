num = str(input())
no_lists = []
yes_lists = []
flag = False
index = 0

for i in num:
	if i == "<" and flag == False:
		flag = True  # < 일때
		print(yes_lists)

	if flag == False: yes_lists.append(i)
	if flag == True: print(i, end='')

	if i == ">" and flag == True:
		flag = False  # > 일떄

print('~~~~~~~~~~~~~~~~```')




print(*yes_lists[yes_lists.index(' ') - 1::-1], end='')

# print(*reversed(yes_lists))

print('-----\n', yes_lists)
# print(yes_lists.index())
# yes_lists.remove(yes_lists[yes_lists.index(' ') - 1::-1])
# yes_lists.remove(yes_lists[yes_lists.index(' ') - 1::-1])
print(*yes_lists[yes_lists.index(' ') - 1::-1], end='')  # 해결
del yes_lists[yes_lists.index(' ') - 1::-1]


print(yes_lists)