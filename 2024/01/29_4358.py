import sys
dicts = {}

while True:

	a = sys.stdin.readline().rstrip()
	if a == '':
		break

	if a not in dicts:
		dicts[a] = 1
	else:
		dicts[a] += 1

dicts = dict(sorted(dicts.items()))
for j, i in zip(dicts.keys(), dicts.values()):
	print(j, "{:.4f}".format((i / sum(dicts.values())) * 100))
