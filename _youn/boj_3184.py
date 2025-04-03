from collections import deque

def check(x, y):
    global R, C
    return 0<=x<R and 0<=y<C

def bfs(start, board, visited):
    queue = deque([start])
    sheep = 1 if board[start[0]][start[1]]=='o' else 0
    wolves = 1 if board[start[0]][start[1]]=='v' else 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if check(nx, ny) and not visited[nx][ny] and board[nx][ny]!='#':
                queue.append((nx, ny))
                visited[nx][ny] = True             
                
                if board[nx][ny]=='o': sheep+=1
                elif board[nx][ny]=='v': wolves+=1

    return ((0, sheep), visited) if sheep>wolves else ((1, wolves), visited)

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
result = [0, 0]

visited = [[False]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j]!='#':
            visited[i][j] = True
            (idx, n), visited = bfs((i, j), board, visited)
            result[idx]+=n
print(*result)