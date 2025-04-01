from sys import stdin as s
from collections import deque
s = open('txt/17086.txt', 'r')

M, N = map(int, s.readline().split())

grid = [list(map(int, s.readline().split())) for _ in range(M)]

max_distance = 0 # 거리는 +1 기준으로 해야됨

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def bfs(i,j):
    visited = [[0] * N for i in range(M)]
    visited[i][j] = True
    q = deque()
    q.append([i,j])

    while q:
        ci, cj = q.popleft()
        for k in range(8):
            ni, nj = ci+dx[k], cj+dy[k]
            if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0: #도달 가능 거리 및 미방문시
                if grid[ni][nj] == 1: # 가장 가까운 아기 상어 발견 시
                    print(visited[ci][cj])
                    return visited[ci][cj] #visited에 저장된 안전거리를 출력 후 종료
                visited[ni][nj] = visited[ci][cj] + 1
                q.append([ni,nj])

for i in range(M):
    for j in range(N):
        if grid[i][j] != 1: # 상어가 있을 경우
            max_distance = max(max_distance , bfs(i,j))#거리 찾기

print(max_distance)

#30m 49s