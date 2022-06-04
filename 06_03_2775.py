
a = int(input())
number_1=0
number_2=0

def DCHA(num):
    return sum(range(1, num + 1))

for i in range(a):
    K = int(input())  # K=층
    T = int(input())  # T=호

    if K>1:
        for k in range(K):
            number_1 += DCHA(T-1)
            number_2 += DCHA(T)

    print(number_1+number_2)