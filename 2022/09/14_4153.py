while (1):
    lists = list(map(int, input().split()))
    if lists[0] == lists[1] == lists[2] == 0: break
    maxs = max(lists)
    lists.remove(max(lists))

    if lists[0] ** 2 + lists[1] ** 2 == maxs ** 2:
        print('right')
    else:
        print('wrong')
