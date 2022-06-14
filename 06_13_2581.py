a=int(input())
b=int(input())
list = []

if a==1 and b==2:   #반례처리
    list.append(b)

if a==b:    #값이 같을떄
    cnt=0
    for j in range(2, a + 1):
        if (a % j == 0):
            cnt += 1
    if (cnt == 1):
        list.append(a)
else:
    for i in range(a,b+1):
        cnt=0
        if(i == 1):
            continue
        for j in range(2, i+1):
            if(i % j == 0):
                cnt += 1
        if(cnt == 1):
            list.append(i)





if len(list)==0:
    print(-1)
    exit()

print(sum(list))
print(min(list))
