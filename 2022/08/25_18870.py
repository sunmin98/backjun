# import sys
# N = sys.stdin.readline()
# lists = []
# ans_lists = []
# sort_lists = []
# index_lists =[]
#
# lists = list(map(int, sys.stdin.readline().split()))
# ans_lists = set(lists)
# ans_lists = list(lists)
# sort_lists = sorted(lists)
#
# #print(sort_lists)
# #print(sort_lists.index(sort_lists[0]))
#
# for i in range(len(sort_lists)):
#     index_lists.append(sort_lists.index(sort_lists[i]))
#
# # index_lists=set(index_lists)
# # index_lists=list(index_lists)
#
# #print(index_lists)
#
# for i in range(len(ans_lists)):
#     for a in range(len(sort_lists)):
#
#         if ans_lists[i] == sort_lists[a]:
#             print(index_lists[a])
#             break
#
# #print(ans_lists)
#
#
#

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

for i in arr:
    print(arr2.index(i), end = ' ')
