a= int(input())

lists=[]

for i in range(a) :
    b = str(input())

    if 50 > len(b) :
        c = ord(b)
        lists.append(c)

print(lists)
print(sorted(lists))
