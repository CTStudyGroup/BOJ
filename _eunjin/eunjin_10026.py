import sys
sys.setrecursionlimit(10000)

# 입력 받기
N = int(input())
matrix = [list(input()) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x):  # 일반 사람용 dfs
    global N, matrix, visited

    if visited[y][x]:
        return
    visited[y][x] = True

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if matrix[ny][nx] == matrix[y][x]:  # 같은 색상인 경우에만 다음 탐색
            dfs(ny, nx)


def dfs2(y, x):  # 적록색약용 dfs
    global N, matrix, visited

    if visited[y][x]:
        return
    visited[y][x] = True

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if matrix[y][x] in ["R", "G"]:
            if matrix[ny][nx] == "B":  # 현재 노드가 R 또는 G이고 다음 노드가 B이면 dfs 실행 안함
                continue
        else:
            if matrix[ny][nx] != "B":  # 현재노드가 B이고 다음 노드가 B가 아니면 dfs 실행 안함
                continue
        #print("curr node:", y, x, ", dfs: ", ny, nx)
        dfs2(ny, nx)


# 일반 dfs 실행
visited = [[False]*N for _ in range(N)]

num1 = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x)
            num1 += 1

# 적록색약 dfs 실행
visited = [[False]*N for _ in range(N)]

num2 = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs2(y, x)
            num2 += 1

print(num1, num2)
