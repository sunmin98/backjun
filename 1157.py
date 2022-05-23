a=str(input()).upper()
lists=[]
count={}
fin=[]

def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)

for i in a:
    lists.append(i)

for num in lists:

        try:
            count[num] += 1
        except:
            count[num] = 1

for i in count:
    if count[i] != 1 : fin.append(i)
    elif len(count)==1: fin.append(i)


if len(fin)!= 1:
    if find_key(count,max(count.values()))!= 1 : print('?')
    else: print(find_key(count,max(count.values())))
elif len(fin)== 1: print(fin[0])

