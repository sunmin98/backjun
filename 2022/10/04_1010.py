import math

a=int(input())

for i in range(a):
    a, b = map(int, input().split())

    if a<b: print(math.comb(b,a))
    elif b<a : print(math.comb(a,b))
    elif a==b : print(1)




