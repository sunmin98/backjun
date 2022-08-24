N=int(input())
arr=[]
count=0
for i in range(N):
    a,b = input().split()
    arr.append((int(a),count,str(b)))
    count+=1

#print(arr)
arr.sort()
#print(arr)

for i in range(N):
    print(arr[i][0],arr[i][2])