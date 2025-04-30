import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
words = set()

for x in range(C):
    temp = ""
    for y in range(R):
        temp += matrix[y][x]
    words.add(temp)

# print(words)

cnt = 0

while(True):
    if cnt == R - 1:
        break

    temp_set = set()
    for word in words:
        temp_set.add(word[cnt + 1:])

    if len(words) != len(temp_set):
        break
    cnt += 1

print(cnt)

