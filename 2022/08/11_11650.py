a = int(input())
lists=[]
lists_s=[]
dic={}

for i in range(0,a):
    lists = list(map(int, input().split()))
    lists_s.append(lists)
    dic[sum(lists_s[i])]=lists_s[i]


print(lists)
print(lists_s)
print(sorted(dic))
print(dic)

for i in sorted(dic):
    print(','.join(dic[i]))



