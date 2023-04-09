import re

a = input()
ans = 0
i = 666
while True:
    i = str(i)
    if re.search(r"666", i):
        ans += 1
        if ans == int(a):
            print(i)
            exit()
    i = int(i)
    i += 1

