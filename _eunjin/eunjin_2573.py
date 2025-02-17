import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
answer = 0


def decrease(y, x):
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if matrix[ny][nx] == 0:
                temp[y][x] += 1


def bfs(y, x):
    global cnt
    q = deque()
    q.append((y, x))
    cnt += 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] != 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True


temp = [[0 for _ in range(M)] for _ in range(N)]
year = 0
while True:
    cnt = 0
    year += 1
    ice_cnt = 0

    visited = [[False]*M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if matrix[y][x] > 0:
                ice_cnt += 1
                decrease(y, x)

    if ice_cnt == 0:
        answer = 0
        break

    for y in range(N):
        for x in range(M):
            if matrix[y][x] > temp[y][x]:
                matrix[y][x] -= temp[y][x]
                temp[y][x] = 0
            else:
                matrix[y][x] = 0
                temp[y][x] = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] > 0 and not visited[y][x]:
                bfs(y, x)

    # print("cnt:", cnt)

    if cnt >= 2:
        answer = year
        break


print(answer)
