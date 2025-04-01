from collections import deque

def isValid(x, y):
    global N, M
    return 0<=x<N and 0<=y<M

def bfs(start):
    global board, N, M
    queue = deque([[start,0]])
    visited = [[False]*M for _ in range(N)]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), d = queue.popleft()
        
        if board[x][y]==1:
            return d

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            nx, ny = x+dx, y+dy
            if isValid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([(nx, ny),d+1])

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = -float('inf')
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            continue
        ans = max(ans, bfs((i,j)))
print(ans)