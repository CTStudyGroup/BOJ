import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

for _ in range(K):
    god_likey = input().strip()
    L = len(god_likey)
    
    dp = [[[-1] * L for _ in range(M)] for _ in range(N)]

    def dfs(y, x, idx):
        if idx == L:
            return 1
        if dp[y][x][idx] != -1:
            return dp[y][x][idx]
        
        cnt = 0
        for d in range(8):
            ny = (y + dy[d] + N) % N
            nx = (x + dx[d] + M) % M
            if board[ny][nx] == god_likey[idx]:
                cnt += dfs(ny, nx, idx + 1)
        
        dp[y][x][idx] = cnt
        return cnt

    total = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == god_likey[0]:
                total += dfs(i, j, 1)

    print(total)
