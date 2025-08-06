import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list((input().strip())) for _ in range(N)]
print(board)
# 사전 정의
d = [[0,1], [1,0], [0,-1], [-1,0]]
visited=[[0]*M for _ in range(N)]

def dfs(y, x, char, starty, startx, depth) :
    # 종료 조건
    if visited[y][x] :
        if depth >= 4 :
            return True
        else :
            return False
    visited[y][x] = 1
    for dy, dx in d :
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == char:
            if (ny, nx) == (starty, startx):
                continue
            if dfs(ny, nx,char, y, x, depth + 1):
                return True
    return False


for i in range(N):
    for j in range(M):
        visited = [[0]*M for _ in range(N)]
        if dfs(i, j, board[i][j], -1, -1, 1):
            print("Yes")
            sys.exit()
print("No")
