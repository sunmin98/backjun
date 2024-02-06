import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)
cnt = 0

while True:
    line = input().rstrip()
    if not line:
        break
    dic[line] += 1
    cnt += 1

for k, v in sorted(dic.items()):
    print('%s %.4f'%(k, v/cnt * 100))