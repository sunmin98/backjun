a, b = map(int, input().split())

for num in range(a, b+1):
    pan=0

    for i in range(2,num+1):
        if num % i == 0:  #나누어 떨어진다는뜻
            pan=1
        # if num==a and num % a ==0:
        #     pan=0

    if pan == 0 :
        print(num)




