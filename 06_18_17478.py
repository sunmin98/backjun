a = int(input())


#    ____
def JH():
    print('"재귀함수가 뭔가요?"')
    return
def JH1():
    print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    return
def JH2():
    print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
def JH3():
    print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')


def JH4():
    print('"재귀함수는 자기 자신을 호출하는 함수라네"')
def JH5():
    print("라고 답변하였지.")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")  # 이거는 꼭 들어가야할거

for i in range(0,a):
    print("____"*i,end=''),JH()
    print("____" * i, end=''), JH1()
    print("____" * i, end=''), JH2()
    print("____" * i, end=''), JH3()

print("____"*a,end=''),JH()
print("____"*a,end=''),JH4()

while True:
    if a==0:
        JH5()
        break
    print("____"*a,end=''),JH5()
    a-=1
