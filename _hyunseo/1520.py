import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 세로 크기 M, 가로 크기 N
M, N = map(int, input().split())
grid = []
for _ in range(M) :
    grid.append(list(map(int, input().split())))
dp = [[-1]*N for _ in range(M)]
#경로 수
answer = 0 
dir = [[0,1], [1,0], [0,-1], [-1,0]]
def dfs(y, x ) :
    print( y, x)
    for line in dp :
        print(line)
    global answer
    if y == M-1 and x ==N-1 :
        return 1
    if dp[y][x] != -1 :
        return dp[y][x]
    
    total = 0
    for d in range(4) :
        ny, nx = y +dir[d][0], x + dir[d][1]
        if 0 <= ny < M and 0 <= nx < N :
            if grid[y][x] > grid[ny][nx] :
                total += dfs(ny, nx)
    dp[y][x] = total
                
    return total

dfs(0, 0)
print(dp[0][0])
