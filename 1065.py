#포기포기

a = int(input())
count=0

for k in range(1,a):
    num = []
    number = []

#숫자 자리별로 대입 num
    for j in str(k):
        num.append(int(j))



#자리별로 빼서 대입   number
    for i in range(0,len(num)):
        if i == len(num)-1: continue
        elif len(num)==1 or len(num) ==2 : number.append(num[i])
        elif len(num)>=3: number.append(num[i]-num[1+i])



#등차수열인지 확인   count
    if len(num)==1 or len(num)==2 : count+=1
    elif number[1]==number[2] and number[2]==number[3]: count+=1
    elif len(number)==2: count+=1


