a= int(input())

num1=0
num2=1
num3=0

if a==1 :
    print(1)
    quit()


for i in range(1,a):
    num3 = num1 + num2

    num1 = num2
    num2 = num3

print(num3)

