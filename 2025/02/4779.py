import sys
import math


def func(start, length):
	if length == 1:
		return

	left = length // 3 + start
	right = (length // 3 * 2) + start

	for i in range(left, right):
		lists[i] = " "

	func(right, length // 3)  # 오른쪽
	func(left - length // 3, length // 3)  # 왼쪽

	return

for line in sys.stdin:
    num = int(line.strip())
    a = '-' * int(math.pow(3, num))
    lists = list(a)  # 리스트 변환
    lists_len = len(lists)

    func(0, lists_len)

    print("".join(lists))