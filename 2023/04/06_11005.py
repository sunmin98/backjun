a, b = map(int, input().split())
lists = []
while True:
    lists.append(a % b)
    a = a // b

    if a == 0:
        break
lists = reversed(lists)

for i in lists:
    if i == 10:
        print('A', end='')
    elif i == 11:
        print('B', end='')
    elif i == 12:
        print('C', end='')
    elif i == 13:
        print('D', end='')
    elif i == 14:
        print('E', end='')
    elif i == 15:
        print('F', end='')
    elif i == 16:
        print('G', end='')
    elif i == 17:
        print('H', end='')
    elif i == 18:
        print('I', end='')
    elif i == 19:
        print('J', end='')
    elif i == 20:
        print('K', end='')
    elif i == 21:
        print('L', end='')
    elif i == 22:
        print('M', end='')
    elif i == 23:
        print('N', end='')
    elif i == 24:
        print('O', end='')
    elif i == 25:
        print('P', end='')
    elif i == 26:
        print('Q', end='')
    elif i == 27:
        print('R', end='')
    elif i == 28:
        print('S', end='')
    elif i == 29:
        print('T', end='')
    elif i == 30:
        print('U', end='')
    elif i == 31:
        print('V', end='')
    elif i == 32:
        print('W', end='')
    elif i == 33:
        print('X', end='')
    elif i == 34:
        print('Y', end='')
    elif i == 35:
        print('Z', end='')
    else:
        print(i, end='')
