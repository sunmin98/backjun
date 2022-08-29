a,b = map(int,input().split())

list_1 = []
list_2 = []
count=0

for i in range(a):
    list_1.append(input())
for i in range(b):
    list_2.append(input())

for i in list_2:
    if i in list_1:
        count+=1

#print(list_1,list_2)
print(count)


