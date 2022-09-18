a = int(input())

max_height = 0  # 가장 긴 높이를 저장할 변수 3,4
max_width = 0  # 가장 긴 가로길이를 저장할 변수 1,2
max_width_index = []  # 가장 긴 가로길이의 인덱스를 저장할 변수 1 2
max_height_index = []  # 가장 긴 높이의 인덱스를 저장할 변수 3 4

lists = []  # 변의 정보들을 저장할 리스트
for i in range(6):
    lists.append(list(map(int, input().split())))

for i in range(6):
    if lists[i][0]==3 or lists[i][0]==4 : max_width_index.append(lists[i][1])

max_width=max(max_width_index)
print(max_width)

for i in range(6):
    if lists[i][0]==1 or lists[i][0]==2 : max_height_index.append(lists[i][1])


print(max_width_index)
print(max_height_index)
print(lists)





