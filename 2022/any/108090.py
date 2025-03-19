a = str(input())

num=[-1 for i in range(26)]
count=1


for i in a:
    for k in (range(97 , 122)):
        if i == chr(k) :
            if num[k-97] == -1 : num[k-97] += count
            elif num[k-97] != -1 : continue

    count+=1


result = ' '.join(map(str, num))
print(result)

