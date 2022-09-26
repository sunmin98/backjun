x, y, w, h = map(int, input().split())

list_1 = [x, y, w - x, h - y]

print(min(list_1))
