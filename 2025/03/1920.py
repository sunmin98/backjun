import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))  # 집합(Set) 사용
M = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().split()))

A = set(A)

for i in X:
	# print(i, A)
	if i in A:
		print("1")
	else:
		print("0")

# print(N)
# print(A)
# print(M)
# print(X)
