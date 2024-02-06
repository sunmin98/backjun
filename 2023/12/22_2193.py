num = int(input())

lists = [0] * 90
# print(lists)
lists[0] = 1
lists[1] = 1
lists[2] = 2
lists[3] = 3

# print(lists)

for i in range(4,90):

	lists[i] = lists[i-1] + lists[i-2]

print(lists[num-1])