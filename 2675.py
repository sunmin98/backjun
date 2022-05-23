
a=int(input())  #몇개입력하는지

for i in range(a):
    D1, D2 = input().split()    #D1 몇번 반복하는지    D2문자열 입력
    D1=int(D1)
    for num in D2:
        for number in range(D1):
            print(num, end='')
