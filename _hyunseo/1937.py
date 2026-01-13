import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
grid = []
for _ in range(n) :
    grid.append(list(map(int, input().split())))
answer = 0
dp = [[-1]*n for _ in range(n)]


def dfs(y,x ) :

    if dp[y][x] != -1 :
        return dp[y][x]
    dp[y][x] = 1
    d = [[-1,0], [1,0], [0,1], [0,-1]]
    for t in range(4) :
        dy, dx = y + d[t][0], x + d[t][1]
        if 0 <= dy < n and 0 <= dx < n :
            if grid[dy][dx] <  grid[y][x] :
                dp[y][x] = max(dp[y][x] , dfs(dy, dx) + 1)
        
    return dp[y][x]
for y in range(n) :
    for x in range(n) :
        answer = max(answer, dfs(y,x))

print(answer)
