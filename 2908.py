D1,D2= map(str, input().split())
a=str()
lists=[]
D1lists=[]
endD1=[]
D2lists=[]
endD2=[]


for num in D1:
    D1lists.append(num)
for i in D1lists[::-1]:
    endD1.append(i)

for num in D2:
    D2lists.append(num)
for i in D2lists[::-1]:
    endD2.append(i)


finD1="".join(endD1)
finD2="".join(endD2)

if finD1>finD2:
    print(finD1)
elif finD2>finD1:
    print(finD2)


