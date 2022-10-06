import math

a = int(input())
lists = []
num = math.factorial(a)
ans = 0

for i in str(num):
    lists.append(i)

lists_mirror = lists[::-1]

for i in lists_mirror:
    if i == '0':
        ans += 1
    else:
        break

print(ans)
