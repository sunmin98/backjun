n = int(input())

for i in range(n):
    c=1
    num = 0
    b=input()
    data=list(b)

    for i in data:
        if i == 'O':
            num+=c
            c+=1
        else:c=1

    print(num)





