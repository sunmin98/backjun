
import sys
n = int(sys.stdin.readline())

for i in range(2,n+1):
    print(' '*(n-i),"*"*(i-1))

print('*'*n)

