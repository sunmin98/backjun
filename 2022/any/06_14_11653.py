a=int(input())

while a!=1 :
#
    for i in range(2,a+1):
        if a%i==0 :
            print(i)
            a=a//i
            break


