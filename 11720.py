a=int(input())
b=str(input(a))
n_list=list(b)
num_list= list(map(int, n_list))
num=0

for i in num_list:
    num+=i

print(num)