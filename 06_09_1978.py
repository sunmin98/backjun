a= int(input())
n1,n2,n3,n4 = map(int, input().split())
li=[]
li.append(n1)
li.append(n2)
li.append(n3)
li.append(n4)

NS_count=0 #소수
count=0 #소수아님

for i in li:
    for num in range(2,i+1):
        if i ==1 :
            count+=1
            break
        if i%num==0 :
            NS_count+=1 #소수라는뜻
            break

print(NS_count,count)
