D1,D2,D3 = map(int, input().split())

if D2>=D3: print(-1)
else: print(D1//(D3-D2)+1)

