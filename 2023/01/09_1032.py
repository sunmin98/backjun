

n = int(input())
a = list(input())
a_len = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))

######################################################################

count = int(input())                # 정수 입력(count)

a = list(input())                   # 처음 입력하는 문자열(리스트)
a_len = len(a)                      # a 리스트의 길이

for i in range(0, count-1):         # 이미 한 차례 입력받았기 때문에, count-1 만큼 새로 입력
    b = list(input())
    for j in range(0, a_len):
        if a[j] != b[j]:
            a[j] = '?'

print("".join(a))


