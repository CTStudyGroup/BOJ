from collections import deque

def bfs(start, end, board):
    global N, M
    
    for n in range(1, N*M):
        queue = deque([start])
        visited = [[None]*M for _ in range(N)]

        while queue:
            x, y = queue.popleft()

            if board[x][y]=='#' and (x,y)==end:
                return n

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if board[nx][ny]=='1':
                        board[nx][ny] = '0'
                    else:
                        queue.append((nx, ny))

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
board = [list(input()) for _ in range(N)]
print(bfs((x1-1, y1-1), (x2-1, y2-1), board))