import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
curr_y, curr_x, curr_dir = map(int, input().split())
dst_y, dst_x, dst_dir = map(int, input().split())
curr_y, curr_x, dst_y, dst_x = curr_y -1 , curr_x - 1, dst_y -1 , dst_x -1
# dir 편리하게 바꾸기
dir = [0,0,2,1,3]
curr_dir , dst_dir = dir[curr_dir], dir[dst_dir]

d = [[0,1], [1,0], [0,-1], [-1,0]]
q = deque()
visited = [[[N*M for _ in range(4)] for _ in range(N)] for _ in range(M)]
visited[curr_y][curr_x][curr_dir] = 0

# y좌표, x좌표, 방향, 지금까지 움직인 횟수, 직전 move, visited
q.append((curr_y, curr_x, curr_dir) )

while q :
    y, x, dir= q.popleft()
    depth = visited[y][x][dir]
    # 종료 조건
    if y==dst_y and x == dst_x and dir == dst_dir:
        print(depth)
        exit()
    
    # 전진 
    for i in range(1, 4) :
        ny, nx = y + d[dir][0]*i, x + d[dir][1]*i
        if ny <0 or ny >= M or nx < 0 or nx >= N : break
        # 도중에 벽이 있으면 move는 불가능
        if board[ny][nx] == 1 :
            break
        if visited[ny][nx][dir] == N*M :
            visited[ny][nx][dir] = depth + 1
            q.append((ny, nx, dir))
            
    # 왼쪽 회전 
    if visited[y][x][(dir-1)%4] == N*M :
        visited[y][x][(dir-1)%4] =  depth + 1 
        q.append((y, x, (dir-1)%4))
        
    # 오른쪽 회전 
    if visited[y][x][(dir+1)%4] == N*M:
        visited[y][x][(dir+1)%4] =  depth + 1 
        q.append((y,x,(dir+1)%4))
