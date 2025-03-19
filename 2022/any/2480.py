D1,D2,D3 = map(int, input().split())

if D1 == D2 == D3:
    num_1 = 10000 + D1 * 1000
    print(num_1)
    quit(0)

if D1 == D2 or D1 == D3 or D2 == D3:
    if D1==D2:
        num_2 = 1000 + D1*100
        print(num_2)
    if D1==D3:
        num_2 = 1000 + D1*100
        print(num_2)
    if D2==D3:
        num_2 = 1000 + D2*100
        print(num_2)

if D1 != D2 and D1 != D3 and D2 != D3:
    arr=[D1,D2,D3]
    max_num=max(arr)
    print(max_num*100)
