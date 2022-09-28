a, b = map(int, input().split())
num = 0
count = 0


def Gcd(a, b):
    if a % b == 0:
        return b
    else:
        return Gcd(b, a % b)

c=Gcd(a,b)
print(c)

print(int(a*b/c))