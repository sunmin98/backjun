a, b = map(int, input().split())

num = list(map(int, input().split(' ')))

list = []	#계산한것들 모음

for i in range(a) :
    for n in range(i+1,a) :
        for m in range(n+1,a) :

            if num[i] + num[n] + num[m] > b : continue
            else : list.append(num[i] + num[n] + num[m])

print(max(list))

# list.sort()
# print(list)
#
# print(list[len(list)-1])

