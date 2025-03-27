import sys
from itertools import permutations
from collections import deque

cube = []
for _ in range(5):
    board = [list(map(int, input().split())) for _ in range(5)]
    cube.append(board)

temp = [[[0] * 5 for _ in range(5)] for _ in range(5)]  # 큐브 임시 저장
answer = sys.maxsize

dz = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]

# matrix를 시계방향으로 회전
def rotate(matrix):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][4 - i] = matrix[i][j]
    return tmp


def dfs(depth):
    global temp
    if depth == 5:
        if temp[4][4][4]:  # 도착 가능할 때에만
            bfs(temp)
        return

    for i in range(4):
        if temp[0][0][0]:  # 출발 가능할 때에만
            dfs(depth + 1)
        temp[depth] = rotate(temp[depth])  # 회전


def bfs(board):
    global answer

    q = deque()
    dist = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    q.append((0, 0, 0))
    while q:
        z, y, x = q.popleft()

        if (z, y, x) == (4, 4, 4):
            answer = min(answer, dist[4][4][4])
            if answer == 12:  # 최소 경로이면 바로 탐색 종료
                print(answer)
                exit()
            return

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nz < 0 or nz >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            elif board[nz][ny][nx] == 0 or dist[nz][ny][nx] != 0:
                continue
            q.append((nz, ny, nx))
            dist[nz][ny][nx] = dist[z][y][x] + 1


for perm in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        temp[perm[i]] = cube[i]
    dfs(0)

if answer == sys.maxsize:
    answer = -1
print(answer)
