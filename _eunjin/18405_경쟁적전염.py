import sys
input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# print(matrix)

virus = []
for y in range(N):
    for x in range(N):
        if matrix[y][x]:
            virus.append([matrix[y][x], [(y, x)]])

# 바이러스 번호 순으로 정렬
virus.sort(key=lambda x: x[0])

# bfs로 바이러스 전파
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def spread():
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for j in range(len(virus)):
        v, coords = virus[j]
        virus[j][1] = []
        for y, x in coords:
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                if visited[ny][nx]:
                    continue
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = v
                    visited[ny][nx] = True
                    virus[j][1].append((ny, nx))


for _ in range(S):
    spread()
    if matrix[X - 1][Y - 1]:
        print(matrix[X - 1][Y - 1])
        exit()
print(matrix[X - 1][Y - 1])

