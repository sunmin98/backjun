num = int(input())  # 진짜 약수의 개수

lists = list(map(int, input().split()))  # 진짜 약수

print(min(lists) * max(lists))
