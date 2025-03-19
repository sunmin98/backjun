#이거 조리시간을 1000분허면 생시는 문제 해결 요

H,M = map(int, input().split())
C=int(input())


if C>60:
    num=C/60
    count=C%60

H+=num
M+=C


if M>=60:
    M-=60
    if M>=60:
        M-=60
        H+=1
    H+=1
    if H>=24:
        H-=24

print(H,M)



