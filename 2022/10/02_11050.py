import math

a, b = map(int, input().split())
lists = [a]

if a == 0:
    print(0)
    exit()
elif b == 0:
    print(1)
    exit()

for i in range(1, b):
    lists.append(a - i)

# print(lists)
num=1
for i in lists:
    num *=i

# print(num)

print(int(num / math.factorial(b)))

