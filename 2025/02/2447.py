N = int(input())
lists = [["*" for j in range(N)] for i in range(N)]
print(lists)


def Func(x, y, N):
	if N == 1:
		return

	for i in range(3):
		for j in range(3):
			print(x + i * (N // 3), y + j * (N // 3), N)  # 좌표 확인
			if i == 1 and j == 1:
				for a in range(x + i * (N // 3), x + (i + 1) * (N // 3)):
					for b in range(y + j * (N // 3), y + (j + 1) * (N // 3)):
						lists[a][b] = " "
				print("1-1일때 ->", x + i * (N // 3), y + j * (N // 3), N)
				continue  # 공백 블록에서는 재귀 호출하지 않음

			Func(x + i * (N // 3), y + j * (N // 3), N // 3)
	return


Func(0, 0, N)
for row in lists:
	print(''.join(row))  # 리스트를 문자열로 변환하여 출력
