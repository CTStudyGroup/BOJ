from sys import stdin as s
from collections import deque
s = open("txt/23288.txt", 'r')

N, M, K = map(int, s.readline().split())

grid = [list(map(int,s.readline().split())) for _ in range(N)]

dice = [[0,2,0],[4,1,3],[0,5,0],[0,6,0]]

move_d = [[0,1],[1,0],[0,-1],[-1,0]] # 동 남 서 북 -> 90도

def turn_dice(d): # 주사위 회전 후 상태
    if d == 0: # 가로 이동 시
        dice[1][2], dice[1][1], dice[1][0], dice[3][1] = dice[1][1], dice[1][0], dice[3][1], dice[1][2]

    if d == 1:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

    if d == 2:
        dice[1][2], dice[1][1], dice[1][0], dice[3][1] = dice[3][1], dice[1][2],dice[1][1], dice[1][0]

    if d == 3:  # 세로 이동 시
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visited = [[0] * M for _ in range(N)] # 같은 곳에서 bfs를 동작할 수 있으니 매번 다시 생성
    visited[i][j] = 1
    current_value = grid[i][j]
    c = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + move_d[k][0]
            ny = y + move_d[k][1]
            #print(nx, ny, visited[nx][ny], grid[nx][ny])
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and grid[nx][ny] == current_value: # 동서남북 연속으로 이동할 수 있을 때
                #print("통과", nx, ny,  visited[nx][ny], grid[nx][ny])
                c += 1
                visited[nx][ny] = 1
                q.append([nx,ny])
    return c

d = 0 # 초기 동쪽
x, y = 0,0 # 초기 주사위 위치
result = 0
for i in range(K):
    #print(d)
    nx = x + move_d[d][0]
    ny = y + move_d[d][1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M: # 맵을 벗어날 경우 반대 방향으로 전환
        #print("반대전환",nx,ny)
        d = (d+2) % 4
        nx = x + move_d[d][0]
        ny = y + move_d[d][1]

    turn_dice(d) # 주사위 상태 변경
    down = dice[3][1]
    if down > grid[nx][ny]: # 이동 방향 90도 회전
        #print("회전" ,d,nx,ny)
        d = (d+1) % 4
        #print("회전 후", d,nx,ny)
    elif down < grid[nx][ny]: # 이동 방향 -90도 회전
        #print("역회전")
        d -= 1
        if d < 0:
            d += 4
    B = grid[nx][ny]
    C = bfs(nx,ny) # 해당 지점에서 동서남북으로 연속이동 가능한 칸의 개수를 구함

    result += B * C # 정답 갱신

    x,y = nx,ny # 주사위 위치 갱신
    #print("현재 번호", i+1 ,"현재 위치 : ",x,y ,"회전 변수", d , "down", down, grid[nx][ny], down > grid[nx][ny], B*C )
print(result)