import math

a = int(input())
lists = []

lists = list(map(int, input().split()))

for i in range(1, len(lists)):
    c = math.gcd(lists[i], lists[0])
    num = lists[i] * lists[0] / c

    print("%d/%d" % (lists[0] / c, lists[i] / c))