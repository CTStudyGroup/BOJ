import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()

        # 목표 지점 도착
        if x == N-1 and y == M-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 벽 부수지 않고 이동
                if matrix[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w]+1
                    q.append([nx, ny, w])

                # 벽 부수고 이동
                elif matrix[nx][ny] == 1 and w == 0:
                    visited[nx][ny][1] = visited[x][y][w]+1
                    q.append([nx, ny, 1])

    return -1


print(bfs())
