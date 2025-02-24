N = int(input())

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

matrix = [[0]*101 for _ in range(101)]

# 커브 표현
for _ in range(N):
    y, x, d, g = map(int, input().split())

    matrix[y][x] = 1

    # 커브 리스트
    dirr = [d]
    for _ in range(g):
        for i in range(len(dirr)-1, -1, -1):
            dirr.append((dirr[i]+1) % 4)
    # print(dirr)

    # 커브 만들기
    for i in range(len(dirr)):
        y += dy[dirr[i]]
        x += dx[dirr[i]]
        if 0 <= y < 101 and 0 <= x < 101:
            matrix[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i+1][j] and matrix[i][j+1] and matrix[i+1][j+1]:
            cnt += 1

print(cnt)
