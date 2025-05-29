import sys

def isBlocked(i, j, visited, N, M):
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i+dx, j+dy
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]: return True
    return False

def solve(depth, total, idx):
    global ans, visited, board, N, M, K
    if depth == K: # base case
        ans = max(ans, total)
        return
    
    for pos in range(idx, N*M):
        i, j = divmod(pos, M)

        if visited[i][j]: continue
        if isBlocked(i, j, visited, N, M): continue

        visited[i][j] = True
        solve(depth+1, total + board[i][j], pos+1)
        visited[i][j] = False
        

N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split()))\
         for _ in range(N)]
ans = -float('inf')
visited = [[False]*M for _ in range(N)]
solve(0, 0, 0)
print(ans)