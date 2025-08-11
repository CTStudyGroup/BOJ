from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 가장자리에서 bfs 시작, 각 치즈 좌표마다 방문 횟수 구하기
# 방문 횟수가 2 이상이면 해당 치즈 좌표는 녹는 좌표로 취급

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs():
    q = deque()
    q.append((0, 0))  # y,x
    visited[0][0] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if matrix[ny][nx] == 0:
                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
            else:  # 치즈
                visited[ny][nx] += 1  # 방문 횟수 추가

def remove_cheese():
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and visited[y][x] >= 2:
                matrix[y][x] = 0

def has_cheese():
    ret = 0
    for row in matrix:
        ret += sum(row)
    return ret

answer = 0
while has_cheese():
    visited = [[0] * M for _ in range(N)]
    bfs()
    remove_cheese()
    answer += 1

print(answer)
