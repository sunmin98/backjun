a, b = map(int, input().split())
list=[]

for i in range(a,b+1):
    list.append(i)

for i in list: #i가 나누어짐 당하는애
    if i % 2 == 0 : list.remove(i)
    if i % 3 == 0 : list.remove(i)
    if i % 5 == 0 : list.remove(i)
    if i % 7 == 0 : list.remove(i)

print(list)

# for i in range(a,b+1):
#     #i 는 차례로 나오는 주인공
#     cnt = 0 #소수인지아닌지
#     if(i == 1): # 1은 소수가 아니기 때문에 건너띔
#         continue
#     for j in range(2, i+1): #j는 소수 나누는에
#         if(i % j == 0): #나누어진다는거는 소수
#             cnt += 1  #소수 마킹
#     if(cnt == 1): #소수라는거
#         print(i)
