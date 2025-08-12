R, C, K = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

# dfs로 갈 수 있는 모든 경로 다 가보고 가짓수 업데이트
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x, depth):
    global answer
    if visited[y][x]:
        return

    if y == 0 and x == C - 1:
        if depth == K:
            answer += 1
        return

    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < R and 0 <= nx < C:
            if matrix[ny][nx] == '.' and not visited[ny][nx]:
                dfs(ny, nx, depth + 1)
                visited[ny][nx] = False

answer = 0
visited = [[False] * C for _ in range(R)]

dfs(R - 1, 0, 1)
print(answer)
