a = []
num = []

for i in range(0, 10):
    a.append(int(input()))
    num.append(a[i]%42)

print(len(set(num)))

#이거 셋을 몰라서 2시간동안 set을 만지고있었다 이래도 되나???
# for i in range(0,10):
#     for k in range(0 , b):
#
#         if num[i] == num[b-k+i]: count.append(num[i])
#         b-=1
#
#     print(count)

