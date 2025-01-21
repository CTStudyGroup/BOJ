import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def fire():  # 불 번지기
    global W, H, matrix, fire_q

    l = len(fire_q)
    for _ in range(l):
        y, x = fire_q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny >= 0 and ny < H and nx >= 0 and nx < W:
                if matrix[ny][nx] in [".", "@"]:
                    fire_q.append((ny, nx))
                    matrix[ny][nx] = "*"


def bfs(start_y, start_x):
    global W, H, matrix, fire_matrix
    q = deque()
    visited = [[False]*W for _ in range(H)]

    q.append((start_y, start_x, 0))
    visited[start_y][start_x] = True

    D = 0
    fire()

    while q:
        y, x, d = q.popleft()

        if d > D:
            D += 1
            fire()

        # print("d:", d, ", fire:", fire_list)

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:  # 탈출
                return d+1
            if matrix[ny][nx] == "#" or visited[ny][nx] or matrix[ny][nx] == "*":
                continue

            q.append((ny, nx, d+1))
            # print("append ny:", ny, ", nx:", nx, ", d:", d+1)
            visited[ny][nx] = True

    return "IMPOSSIBLE"


for _ in range(T):
    W, H = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(H)]

    start_y, start_x = 0, 0
    fire_q = deque()

    for h in range(H):
        for w in range(W):
            if matrix[h][w] == "@":
                start_y, start_x = h, w
            if matrix[h][w] == "*":
                fire_q.append((h, w))

            # print(matrix)
            # print(firelist())
    print(bfs(start_y, start_x))
