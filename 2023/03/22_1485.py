import math

answer_TF = bool
num = int(input())
answer = []
for i in range(num):
    lists = []
    for i2 in range(4):
        a, b = map(int, input().split())
        lists.append([a, b])

    sort_list = sorted(lists)

    # print(sort_list)
    one_three = math.sqrt(((sort_list[0][0] - sort_list[2][0]) ** 2) + ((sort_list[0][1]) - sort_list[2][1]) ** 2)
    two_four = math.sqrt(((sort_list[1][0] - sort_list[3][0]) ** 2) + ((sort_list[1][1]) - sort_list[3][1]) ** 2)

    if one_three == two_four:
        if sort_list[0][0] - sort_list[1][0] == sort_list[0][0] - sort_list[0][1] == sort_list[0][0] - sort_list[0][1] ==  : answer_TF = True
        
    else:
        answer.append(0)

for i in answer:
    print(i)
