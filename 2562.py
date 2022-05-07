b=list()

for i in range(0,9):
    b.append(int(input()))

print(max(b))
print(b.index(max(b))+1)

