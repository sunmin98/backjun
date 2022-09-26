lists_num=[]

def solution(lists):

    max_s = 0

    for i in range(len(lists)):
        if lists[i][0] > max_s : max_s = lists[i][0]

    for i in range(0, max_s):
        globals()["num{}".format(i)] = i


lists=[[2,10],[7,1],[2,5],[2,9],[7,32]]


solution(lists)



