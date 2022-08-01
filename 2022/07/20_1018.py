# width, height = map(int, input().split())
#
# id=0
# lists=[]
# string=str()
#
# string=input(str())
# lists=list(string)
#
# #print(lists)
# for i in range(0,len(lists)-1) :
#     if lists[i]=='W' and lists[i+1]=='W' : id+=1
#
#     if lists[i]=='B' and lists[i+1]=='B' : id+=1
# print(id//2)

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)