a=str(input())
lists=[]
count=0

for num in a:
    lists.append(num)


if lists[0]!= " " : count+=1
if lists[len(lists)-1] ==" " : count-=1

for i in lists:
    if i==" ": count+=1

print(count)
