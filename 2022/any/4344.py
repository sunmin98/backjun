n = int(input())

for i in range(0,n):
    count=0
    num=list(map(int, input().split()))
    aver=(sum(num)-num[0])/(len(num)-1)


    for i in range(1,len(num)):

        if num[i]>aver: count+=1

    print(round(count/(len(num)-1)*100,3),"%")

