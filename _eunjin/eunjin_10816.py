# 입력 받기
M = int(input())
cards = list(input().split())
M = int(input())
find = list(input().split())

d = {}

for card in cards:
    if card in d:
        d[card] += 1
    else:
        d[card] = 1

# print(d)

for x in find:
    if x in d:
        print(d[x], end=" ")
    else:
        print(0, end=" ")
