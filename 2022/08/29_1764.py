a, b = map(int, input().split())

list_1 = []
list_2 = []
list_3 = []

for i in range(a):
    num = str(input())
    list_1.append(num)

for i in range(b):
    num = str(input())
    list_2.append(num)

list_3 = set(list_1) & set(list_2)

print(len(list_3))

for i in sorted(list_3):
    print(i)

# for i in range(b):
#     num=str(input())
#     list_2.append(num)
# list_2=set(list_2)
# list_2=list(list_2)

# print(list_1,list_2)

# for i in list_1:
#     if i in list_2:
#         list_3.append(i)
#
# print(len(list_3))
# #print(list_3)
# for i in list_3:
#     print(sorted(list_3))
