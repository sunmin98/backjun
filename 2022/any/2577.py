a = int(input())
b = int(input())
c = int(input())

d = a * b * c

int(d)
num = len(str(d))-1

re = list()
arr=[0 for i in range(10)]


for i in range(num+1):
    re.append(d//(10**(num-i)))
    d -= 10**(num-i)*re[i]
    for k in range(0,10):
        if re[i] == k: arr[k]+=1


for i in range(10):
    print(arr[i])