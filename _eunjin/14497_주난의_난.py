from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def print_matrix():
    print("--------------------")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

# bfs
# 파동은 상하좌우 각 방향에 대해서 1을 만날 때까지 계속 퍼진다.
def bfs():
    global matrix
    visited = [[False] * M for _ in range(N)]

    q = deque()
    q.append((x1 - 1, y1 - 1))
    visited[x1 - 1][y1 - 1] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if visited[ny][nx]:
                continue

            if matrix[ny][nx] == "0":
                q.append((ny, nx))
                visited[ny][nx] = True
            elif matrix[ny][nx] == "1":
                matrix[ny][nx] = "_"
                visited[ny][nx] = True
            elif matrix[ny][nx] == "#":
                return True  # 이번 bfs 탐색에서 # 찾으면 True를 리턴

    return False  # 이번 bfs 탐색에서 # 못 찾으면 False를 리턴

def update():
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == "_":
                matrix[y][x] = "0"

T = 0
while True:
    T += 1

    # 접프
    found = bfs()

    if found:
        print(T)
        break

    # _를 0으로 변경
    update()
