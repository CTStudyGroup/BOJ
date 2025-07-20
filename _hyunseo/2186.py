
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(input().strip()))


goal_word = list(input().strip())
answer = 0
dp = [[[-1 for _ in range(len(goal_word))] for _ in range(M)] for _ in range(N)]
d = [[1,0],[0,1],[-1,0],[0,-1]]
def dfs(y,x,idx) :

    if idx == len(goal_word) -1:
        return 1
    if dp[y][x][idx] != -1 :
        return dp[y][x][idx]
    dp[y][x][idx] = 0
    for dir in range(4) :
        for dist in range(1, K+1) :
            ny = y + d[dir][0] * dist
            nx = x + d[dir][1] * dist
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == goal_word[idx + 1]:
                dp[y][x][idx] += dfs(ny, nx, idx + 1)
                
    return dp[y][x][idx]
answer = 0

for yy in range(N) :
    for xx in range(M) :
        if board[yy][xx] == goal_word[0] :
            answer += dfs(yy, xx, 0)
print(answer)
