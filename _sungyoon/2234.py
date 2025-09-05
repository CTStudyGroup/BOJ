import sys
from collections import defaultdict

input = sys.stdin.readline

# 세로 M, 가로 N인 board
N, M = map(int, input().split())
board = [['']*N for _ in range(M)]
for i in range(M) :
    inp = list(map(int, input().split()))
    for j, spot in enumerate(inp) :
        # 바이너리로 저장
        bin_spot= bin(spot)[2:]
        # 1 -> Ob1 -> 앞에 0으로 채움 -> 0001
        board[i][j] = '0'*(4-len(bin_spot)) + bin_spot
        
        
d = [[1,0], [0,1], [-1,0], [0,-1]]
# 방문 처리 배열
visited=[[0]*N for _ in range(M)]
# 각각 속한 방 번호
room =[[-1]*N for _ in range(M)]

def dfs(y, x) :
    # 현재 좌표의 벽 상태
    curr_wall = board[y][x]
    
    room[y][x] = number  # 방 번호 부여
    visited[y][x] = 1    # 방문 처리
    '''
   # 처음에는 감이 안 와서 주석 안처럼 구현했지만, 나중에는 단순화했습니다. 
    # 서쪽 벽 비어있음 (0)
    if curr_wall[3] == '0' and 0 < x and visited[y][x-1] == 0 :
        dfs(y, x-1)
    # 동쪽 벽 비어있음 (0)
    if curr_wall[1] == '0' and x < N-1 and visited[y][x+1] == 0 :
        dfs(y, x+1)
    # 북쪽 벽 비어있음 (0) 
    if curr_wall[2] == '0' and 0 < y and visited[y-1][x] == 0 :
        dfs(y-1, x)
    if curr_wall[0] == '0' and y < M-1 and visited[y+1][x] == 0 :
        dfs(y+1, x)
    '''
    for dir  in range(4) :
        ny, nx = y + d[dir][0], x + d[dir][1]
        if curr_wall[dir] =='0' and 0<=ny<M and 0<=nx<N and visited[ny][nx] == 0 :
            dfs(ny, nx)
    
number = 1  # 부여할 방 번호
dic = defaultdict(int)  # 방 번호에 해당하는 방 수 count


for i in range(M) :
    for j in range(N) :
        if visited[i][j] == 0 :
            dfs(i, j)
            number += 1
        dic[room[i][j]] += 1
print(len(dic.keys()))  # 방 수
print(max(dic.values()))  # 제일 큰 방 크기


tmp = list(dic.values()).sort()  # 일찍 끝내기 위한 조건 
tmp_max = tmp[-1] + tmp[-2]

max_combined_room = 0
for i in range(M) :
    for j in range(N) :
        curr = room[i][j]
        for idx in range(4) :
            ny, nx = i + d[idx][0], j + d[idx][1]
            if 0<= ny < M and 0 <= nx < N :
                next_room= room[ny][nx]
                
                # 만약 합칠 수 있는 방이면
                if curr != next_room :
                    max_combined_room = max( max_combined_room, dic[curr] + dic[next_room])
                    
                    # 일찍 끝내기 위한 조건
                    if max_combined_room == tmp_max :
                        print(max_combined_room)
                        sys.exit()
print(max_combined_room)
