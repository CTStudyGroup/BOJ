import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]

# R*C 완전탐색
# #를 만나면 temp를 arr에 저장하고 temp 비우기

words = set()  # 가능한 모든 낱말

# 가로 방향
for y in range(R):
    temp = ""
    for x in range(C):
        if matrix[y][x] == "#":
            if len(temp) >= 2:
                words.add(temp)
            temp = ""
        else:
            temp += matrix[y][x]
    if len(temp) >= 2:
        words.add(temp)

# 세로 방향
for x in range(C):
    temp = ""
    for y in range(R):
        if matrix[y][x] == "#":
            if len(temp) >= 2:
                words.add(temp)
            temp = ""
        else:
            temp += matrix[y][x]
    if len(temp) >= 2:
        words.add(temp)

sorted_words = sorted(list(words))
print(sorted_words[0])
