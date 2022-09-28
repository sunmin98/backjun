import math

a = int(input())

for i in range(a):
    a, b = map(int, input().split())
    x = math.gcd(a, b)
    print(int(a * b / x))
