a=str(input())
num=0

for i in a:
    if i == 'A' or i == 'B' or i == 'C': num += 3
    if i == 'D' or i == 'E' or i == 'F': num += 4
    if i == 'G' or i == 'H' or i == 'I': num += 5
    if i == 'J' or i == 'K' or i == 'L': num += 6
    if i == 'M' or i == 'N' or i == 'O': num += 7
    if i == 'P' or i == 'Q' or i == 'R' or i == 'S': num += 8
    if i == 'T' or i == 'U' or i == 'V': num += 9
    if i == 'W' or i == 'X' or i == 'Y' or i == 'Z': num += 10

print(num)

