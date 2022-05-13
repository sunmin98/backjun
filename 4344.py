n = int(input())

for i in range(1,n+1):
    count=0
    aver=0
    num=list(map(int, input().split()))
    for a in enumerate(num, start=1):
        aver += a[a]
    averegy=aver/(len(num)-1)
    print(averegy)


    # for i in enumerate(num,start=1):
    #     if i>aver : count+=1
    #
    # print(count/(len(num)-1),"%")









