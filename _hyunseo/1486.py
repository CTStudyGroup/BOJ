# A => 65,a=> 97
import sys

input = sys.stdin.readline

N, M, T, D = map(int, input().split())
grid = [[]*M for _ in range(N)]
for n in range(N) :
    s = input().strip()
    for alphabet in list(s) :
        ord_alp = ord(alphabet)
        if ord_alp <= 96 :
            grid[n].append(ord(alphabet)-65)
        else:
            grid[n].append(ord(alphabet)-71)


going_up =  [[D, D]*M for _ in range(N)]
going_up[0][0] = 0

d = [[-1, 0], [0,1], [1,0],[0,-1]]
def dfs_up(y, x, time):
    if going_up[y][x] < time :
        return
    
    for dir in range(4) :
        ny, nx = y + d[dir][0], x + d[dir][1]
        if 0 <= ny < N and 0 <= nx < M :
            if abs(grid[ny][nx] - grid[y][x]) <= T :
                if grid[y][x] < grid[ny][nx] and abs(grid[y][x]- grid[ny][nx]) <= D :
                    nxt_time = time + abs(grid[y][x]- grid[ny][nx])**2
                else :
                    nxt_time = time + 1
                
                if going_up[ny][nx] > nxt_time :
                    going_up[ny][nx] = nxt_time
                    dfs_up(ny, nx, nxt_time)
                        
dfs_up(0,0,0)

import heapq

q = []
for y in range(N) :
    for x in range(M) :
        heapq.heappush(q, [-grid[y][x], going_up[y][x], y, x] )

down = [[D]*M for _ in range(N)]


def going_down(y, x,time, org_y, org_x) :
    if y == 0 and x == 0 :
        down[org_y][org_x] = min(time, down[org_y][org_x])
        return
    
    if tmp[y][x] < time :
        return
    
    for dir in range(4) :
        ny, nx = y + d[dir][0], x + d[dir][1]
        if 0<= ny < N and 0 <= nx < M :
            if abs(grid[ny][nx] - grid[y][x]) <= T :
                # uphill
                if grid[ny][nx] > grid[y][x] : 
                    nxt_time = time + abs(grid[y][x]- grid[ny][nx])**2
                else :
                    nxt_time = time + 1
                
                if tmp[ny][nx] > nxt_time :
                    tmp[ny][nx] = nxt_time
                    going_down(ny, nx, nxt_time, org_y, org_x)

while q :
    highest_spot, up_time, i, j = heapq.heappop(q)
    highest_spot *= -1

    tmp=[[D]*M for _ in range(N)]
    going_down(i, j, 0, i, j)
    if up_time + down[i][j] <= D :
        print(highest_spot)
        sys.exit()
