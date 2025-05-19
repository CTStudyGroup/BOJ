from collections import deque

def isValid(x, y):
    global N, M
    return 0<=x<N and 0<=y<M

def bfs(start, board, visited):
    queue = deque([start])
    count = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x+dx, y+dy
            if isValid(nx, ny) and not visited[nx][ny] and board[nx][ny]==1:
                visited[nx][ny] = True
                count += 1
                queue.append((nx, ny))
    return count

def solve(board):
    ans = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j]==1:
                visited[i][j] = True
                ans = max(ans, bfs((i,j), board, visited))
    return ans

# Input
N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

# Solve
print(solve(board))