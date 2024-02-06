a, b = input().split()
lists = map(int, input().split())
count = 0
tmp = []


def merge_sort(A, p, r):
	if p < r:
		q = (p + r) // 2
		merge_sort(A, p, q)
		merge_sort(A, q + 1, r)
		merge(A, p, q, r)


def merge(A, p, q, r):
	i = p
	j = q + 1
	t = 1

	while i <= 1 and j < r:
		if A[i] <= A[j]:
			tmp[t] = A[i]
			t += 1
			i += 1
		else:
			t += 1
			j += 1

	while i <= q:
		tmp[i] = A[i]
		t += 1
		i += 1
	while j <= r:
		tmp[t] = A[j]
		t += 1
		j += 1

	i = p
	t = 1

	while i <= r:
		A[i] = tmp[t]
		i += 1
		t += 1


merge_sort(lists, 0, a - 1)
print(lists)
