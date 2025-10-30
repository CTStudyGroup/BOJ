import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
grid = []
for _ in range(N) :
    grid.append(list(map(int, input().split())))
q = deque()
q.append([0,0,0])
answer = sys.maxsize
dp = [[sys.maxsize]*N for _ in range(N)]
def move_right(y, x, cnt) :
    if grid[y][x] > grid[y][x+1] and dp[y][x+1] < cnt:
        dp[y][x+1] = cnt
        return ([y, x +1, cnt])

    
while q :
    y, x, cnt = q.popleft()
    if y == N-1 and x == N-1 :
        answer = min(answer, cnt)
        continue
    if dp[y][x] < cnt :
        continue
    if 0<= y < N-1 and 0 <= x < N-1 :
        if grid[y][x] > grid[y][x+1]:
            if dp[y][x+1]> cnt :
                dp[y][x+1] = cnt
                q.append([y, x +1, cnt])
        else :
            if dp[y][x+1] > cnt + abs(grid[y][x]- grid[y][x+1]) + 1 :
                dp[y][x+1] = cnt + abs(grid[y][x]- grid[y][x+1]) + 1
                q.append([y, x+1, cnt + abs(grid[y][x]- grid[y][x+1]) + 1])
        if grid[y][x] > grid[y+1][x] :
            if  dp[y+1][x] > cnt  :
                dp[y+1][x] = cnt
                q.append([y+1, x, cnt])
        else :
            if dp[y+1][x] > cnt + abs(grid[y][x]- grid[y+1][x]) + 1 :
                dp[y+1][x] = cnt + abs(grid[y][x]- grid[y+1][x]) + 1
                q.append([y+1, x, cnt + abs(grid[y][x]- grid[y+1][x]) + 1])
    elif y == N-1 and 0<= x < N-1 :
        if grid[y][x] > grid[y][x+1] :
            if dp[y][x+1] > cnt :
                dp[y][x+1] = cnt
                q.append([y, x+1, cnt ])
        else :
            if dp[y][x+1] > cnt + abs(grid[y][x]- grid[y][x+1]) + 1 :
                dp[y][x+1] = cnt + abs(grid[y][x]- grid[y][x+1]) + 1
                q.append([y, x+1, cnt + abs(grid[y][x] - grid[y][x+1])+1])
    elif 0<= y< N-1 and x == N-1 :
        if grid[y][x] > grid[y+1][x] :
            if dp[y+1][x] > cnt :
                dp[y+1][x] = cnt
                q.append([y+1, x, cnt])
        else :
            if dp[y+1][x] > cnt + abs(grid[y][x]- grid[y+1][x]) + 1 :
                dp[y+1][x] = cnt + abs(grid[y][x]- grid[y+1][x]) + 1
                q.append([y+1, x, cnt + abs(grid[y][x] - grid[y+1][x]) + 1])
print(answer)
