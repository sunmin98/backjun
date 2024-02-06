A = int(input())
ANS = 0
lists = []
CHONG = False
dicts = {}

for i in range(1, A):

	a, b = map(str, input().split())

	if a == "ChongChong":
		if CHONG == True:
			ANS -= 1
		else:
			CHONG = True
			lists = []
	lists.append(a)

	if b == "ChongChong":
		lists = []
		if CHONG == True:
			ANS -= 1
		else:
			CHONG = True
			lists = []
	lists.append(b)

for i in lists:
	dicts[i] = False
dicts["ChongChong"] = True

lists1 = []
for i in range(1, len(lists) - 1, 2):
	lists1.append([lists[i], lists[i + 1]])

dicts[lists1[0][0]] = True

print(lists)
print("\n")
print(lists1[0][0])

# for i in lists1:
# 	print(i[0])

for i in lists1:
	if dicts.get(i[0]) == True :
		dicts[dicts.get(i[1])] = True

print(lists1)
print(dicts)
