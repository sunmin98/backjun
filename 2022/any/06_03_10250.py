a = int(input())

for i in range(a):
    H, W, N = map(int, input().split())
    ans_H = 0
    ans_W = 1
    for h in range(N):
        ans_H += 1
        if ans_H > H:
            ans_H = 1
            ans_W += 1


    print(ans_H*100+ans_W)