import sys

input = sys.stdin.readline

def dfs_down(y, x, path) :
    visited[y][x] = 1
    path += board[y][x]
    if y + 1 < R and board[y+1][x] != "#" :
        dfs_down(y + 1, x , path)
    else :
        if len(path) > 1 :
            words.add(path)
        return

def dfs_side(y, x, path) :
    visited_sideways[y][x] = 1
    path += board[y][x]
    if x + 1 < C  and board[y][x + 1] != "#" :
        dfs_side(y, x+1, path)
    else :
        if len(path) > 1 :
            words.add(path)
        return

R, C = map(int, input().split())
board = []
for _ in range(R) :
    board.append(list(input().strip()))


visited = [[0]*C for _ in range(R)]
visited_sideways = [[0]*C for _ in range(R)]
words = set()
for i in range(R) :
    for j in range(C) :
        if board[i][j]!= "#" and visited[i][j] == 0 :
            dfs_down(i, j, '')
        if board[i][j] != "#" and visited_sideways[i][j] == 0 :
            dfs_side(i, j, '')
words=list(words)
words.sort()
print(words[0])
