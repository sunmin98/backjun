num1, num2, num3, num4, num5, num6 = map(int, input().split())
X = int()
Y = int()
lists = [num1, num2, num3, num4, num5, num6]
lists_ans1 = []
lists_ans2 = []
# num3 = (num1 * X) + (num2 * Y)
# num6 = (num4 * X) + (num5 * Y)

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (num1 * i) + (num2 * j) == num3 and (num4 * i) + (num5 * j) == num6:
            print(i, j)
            exit()

