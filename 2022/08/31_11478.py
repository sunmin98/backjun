a = input()
lists = list(a)
lists_1 = []

number = 1
for i in range(len(a)):
    for j in range(i, len(a)):
        lists_1.append(a[i:j + 1])  # i번째 문자부터 부분문자열 구하기

print(len(set(lists_1)))
