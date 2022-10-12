
import math

a, b = map(int, input().split())
lists = []
num = math.comb(a,b)
ans = 0

for i in str(num):
    lists.append(i)

# lists_mirror = lists[::-1]

for i in lists[::-1]:
    if i == '0':
        ans += 1
        break

print(ans)
