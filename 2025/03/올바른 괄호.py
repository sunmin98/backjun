def solution(s):
	stack = []  # 괄호를 넣을 상자

	for char in s:
		if char == '(':
			# '(' 만나면 상자에 넣기
			stack.append(char)
		else:
			# ')' 만나면 상자에서 '(' 꺼내기
			if len(stack) == 0:  # 상자가 비어 있으면 에러
				return False
			stack.pop()  # '(' 하나 꺼냄

	# 모든 글자를 다 읽은 뒤 상자가 비어 있어야 짝이 맞음
	return len(stack) == 0


# 간단 테스트
print(solution("()()"))  # True
print(solution("(())()"))  # True
print(solution(")()("))  # False
print(solution("(()("))  # False
