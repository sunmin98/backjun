import sys

input = sys.stdin.readline

n, k = map(int, input().split())
k += 1
lists = []
for i in range(n):
	lists.append(int(input()))

lists_1 = [0] * n * k
num = 1
print(lists_1)

for i in range(0, k):
	lists_1[i] = 1

for i in range(k, n * k):
	if i % 10 == 0:
		print(i)
		num += 1
		lists_1[i] = 1
	else:
		lists_1[i] = lists_1[i - 2] + lists_1[i - k]

print(lists_1)
# for i in range(0, k):
# 	lists_1[0][i] = 1
# # print(lists_1)
# num = int(input())
#
# for i in range(1, n):
# 	num = int(input())
# 	for j in range(0, k):
# 		if j - num < 0:
# 			lists_1[i][j] += lists_1[i - 1][j]
# 		else:
# 			lists_1[i][j] = lists_1[i - 1][j] + lists_1[i][j - num]
