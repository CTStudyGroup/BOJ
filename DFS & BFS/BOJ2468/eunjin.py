import sys
sys.setrecursionlimit(100000)


# 입력 받기
N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 물에 잠기지 않는 영역을 나타내는 matrix 생성


def set_safe_matrix(h):
    global matrix, N
    result = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if(matrix[x][y] > h):
                result[x][y] = 1

    return result


def dfs(visited, y, x):
    global safe_matrix
    if(visited[y][x]):
        return

    visited[y][x] = True
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if(0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]) and (safe_matrix[ny][nx] == 1):
            dfs(visited, ny, nx)


cnt_list = []

for h in range(0, 101):
    cnt = 0
    safe_matrix = set_safe_matrix(h)

    visited = [[False for _ in range(N)] for _ in range(N)]
    # for row in safe_matrix:
    #     for elem in row:
    #         print(elem, end=" ")
    #     print()

    for y in range(N):
        for x in range(N):
            if(safe_matrix[y][x] == 1 and not visited[y][x]):
                dfs(visited, y, x)
                # print(visited)
                cnt += 1
    # print(cnt)
    cnt_list.append(cnt)
    # print("====================")

print(max(cnt_list))
