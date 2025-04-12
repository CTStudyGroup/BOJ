import sys
input = sys.stdin.readline
R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]

dy = [-1, 0, 1]
dx = [1, 1, 1]

# (y,x)에서 다음 파이프 칸 연결하기
answer = 0
visited = [[False] * C for _ in range(R)]

def dfs(y, x):
    global answer
    matrix[y][x] = '-'
    if x == C - 1:
        answer += 1
        return True

    for i in range(3):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue
        if matrix[ny][nx] == 'x' or matrix[ny][nx] == '-':
            continue
        if dfs(ny, nx):
            return True

for i in range(R):
    dfs(i, 0)

print(answer)
