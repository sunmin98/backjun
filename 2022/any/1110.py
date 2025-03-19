a = int(input())
count=0
k = a
while (1):
    num=a//10
    num1=a%10
    num2 = num1+num
    if num2>10:
        num2=num2%10

    num3 = num2+(num1*10)
    count += 1
    a=num3
    if k==num3:
        print(count)
        break
