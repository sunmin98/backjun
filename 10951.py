a,b = map(int, input().split())
while (1):

    try:
        print(a+b)
        a, b = map(int, input().split())
    except:
        break
