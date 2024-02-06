text = str(input())
lists = []
dicts = {}

for i in text:
	lists.append(i.upper())

# print(lists)
for i in lists:
	if i in dicts:
		dicts[i] += 1
	else:
		dicts[i] = 1

max_num = max(dicts.values())
ans_lists = [k for k, v in dicts.items() if v == max_num]
# print(ans_lists)

if len(ans_lists) > 1:
	print("?")
else:
	print(ans_lists[0])
