import sys

input = sys.stdin.readline
lists = []


def One(num1):
	lists.append(num1)


def Two():
	if len(lists) > 0:
		print(lists[-1])
		lists.pop()

	elif len(lists) == 0:
		print(-1)


def Three():
	print(len(lists))


def Fourth():
	if len(lists) > 0:
		print(0)
	elif len(lists) == 0:
		print(1)


def Five():
	if len(lists) > 0:
		print(lists[-1])
	elif len(lists) <= 0:
		print(-1)


n = int(input())

for i in range(n):
	num_list = list(map(int, input().split()))
	if num_list[0] == 1:
		One(num_list[1])
	elif num_list[0] == 2:
		Two()
	elif num_list[0] == 3:
		Three()
	elif num_list[0] == 4:
		Fourth()
	elif num_list[0] == 5:
		Five()
