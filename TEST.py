x1 = "343434"
x2 = "333"

print(f"비교: '{x1}' vs '{x2}'\n")

for i in range(min(len(x1), len(x2))):  # 짧은 길이까지만 비교
	print(f"비교 {i + 1}: '{x1[i]}' vs '{x2[i]}'")

	if x1[i] > x2[i]:
		print(f" → '{x1}'이 더 크므로 '{x1[:i + 1]}'까지만 보고 정렬 결정됨!\n")
		break
	elif x1[i] < x2[i]:
		print(f" → '{x2}'이 더 크므로 '{x2[:i + 1]}'까지만 보고 정렬 결정됨!\n")
		break
