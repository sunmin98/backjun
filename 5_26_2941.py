a = str(input())
lists1=[]
lists2=[]
lists3=[]
count=0
''
a1=str
a2=str
a3=str

cro=0

for i in a:
    lists1.append(i)

for i in a:
    lists2.append(i)
del lists2[0]
lists2.insert(len(lists2),"")

for i in a:
    lists3.append(i)
del lists3[0]
del lists3[0]
lists3.insert(len(lists3),"")
lists3.insert(len(lists3),"")

for a1,a2 in zip(lists1,lists2) :
    plus = a1+a2
    if plus in ['c=','c-','d-','lj','nj','s=','z=']: cro+=1

for a1,a2,a3 in zip(lists1,lists2,lists3) :
    plus = a1+a2+a3
    if plus=='dz=': cro+=1

print(len(lists1)-cro)