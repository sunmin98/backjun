a= str(input())
lists = []
b=0
c=0

for i in a:
    lists.append(int(i))

sort_lists=sorted(lists)

for i in sort_lists :

    b+=i*(10**c)
    c+=1

print(b)


