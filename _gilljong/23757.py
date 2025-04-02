from sys import stdin as s
import heapq
s = open("txt/23757.txt", "r")

N, M = map(int, s.readline().split())

gift = list(map(int, s.readline().split()))

child = list(map(int, s.readline().split()))

# 매번 정렬할 때마다, nlogn
h = []
for i in gift:
    heapq.heappush(h, -i)

for i in child:
    value = -(heapq.heappop(h))
    if i <= value:
        value -= i
        heapq.heappush(h,-value)
    else:
        print(0)
        exit()
print(0)
# gift.sort(key = lambda x : -x)
#
# for i in range(len(child)):
#     done = 0
#     for j in range(0,i+1):
#         if child[i] <= gift[j]:
#             gift[j] -= child[i]
#             done = 1
#             break
#     if done == 0:
#         print(0)
#         exit()
#
# print(1)


