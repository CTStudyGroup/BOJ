import sys

input = sys.stdin.readline
from collections import deque

grid = []
for _ in range(3) :
    grid.append(list(map(str, input().strip().split())))
Sgrid = ''.join([''.join(line) for line in grid])

goal = [['1','2','3'],['4','5','6'],['7','8','0']]
Sgoal = ''.join([''.join(line) for line in goal])
visited = set()
        
''.join([''.join(line) for line in goal])


dir = [[0,1], [1,0], [0,-1], [-1,0]]
q = deque()
q.append([Sgrid, 0])

    


while q :
    sgrid, cnt = q.popleft()
    if sgrid == Sgoal :
        print(cnt)
        sys.exit()

    y, x = 0,0
    for i in range(3) :
        for j in range(3) :
            idx = 3*i + j
            grid[i][j] = sgrid[idx]
            if sgrid[idx]== '0' :
                y, x = i, j
    for d in range(4) :
        ny, nx = y + dir[d][0], x + dir[d][1]
        if 0<=ny<3 and 0<=nx<3 :
            grid[ny][nx], grid[y][x] = grid[y][x], grid[ny][nx]
            joined = ''.join([''.join(line) for line in grid])
            if joined not in visited :
                q.append((joined, cnt + 1))
                visited.add(joined)
            grid[ny][nx], grid[y][x] = grid[y][x], grid[ny][nx]
print(-1)         
        
