import sys

input1 = sys.stdin.readline
num = int(input1())
lists = []
lists1 = []

for i in range(num):
	point = int(input1())
	lists.append(point)
lists.reverse()
print(lists)

lists1.append(lists[0])
lists1.append(max(lists[0] + lists[1], lists[0] + lists[2]))
lists1.append(max(lists1[1] + lists[3], lists1[1] + lists[4]))

for i in range(3, num - 1):
	lists1.append(max(lists1[i - 2] + lists[i], lists1[i - 3] + lists[i + 1] + lists[i - 1]))
	print(lists1)
	print(lists[i])  # 20
	print(lists[i + 1])  # 10

print(lists1)

# import sys
#
# input = sys.stdin.readline
# arr = []
# dp = []
#
# l = int(input())
# for _ in range(l):
# 	arr.append(int(input()))
#
# dp.append(arr[0])
# dp.append(max(arr[0] + arr[1], arr[1]))
# dp.append(max(arr[0] + arr[2], arr[1] + arr[2]))
# for i in range(3, l):
# 	dp.append(max(dp[i - 2] + arr[i], dp[i - 3] + arr[i] + arr[i - 1]))
# 	print(dp)
#
# print(dp.pop())
