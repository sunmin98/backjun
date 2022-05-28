a = int(input())
count = a



for i in range(a):
    string = str(input())

    for j in range(0,len(string)-1):
        if string[j]==string[j+1]: pass

        elif string[j] in string[j+1:]:
            count -= 1
            break

print(count)



