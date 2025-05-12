from collections import deque

def isValid(x, y):
    global N, M
    return 0<=x<M and 0<=y<N

def bfs(start, t, board):
    global visited
    queue = deque([start])
    visited[start[0]][start[1]] = True
    num = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if isValid(nx, ny) and not visited[nx][ny] and board[nx][ny]==t:
                queue.append((nx, ny))
                visited[nx][ny] = True
                num+=1     
    return num**2

# Input
N, M = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(input()))

# Solve
visited = [[False]*N for _ in range(M)]
power = {'W':0,'B':0}
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            t = board[i][j]
            power[t] += bfs((i,j), t, board)
print(power['W'],power['B'])