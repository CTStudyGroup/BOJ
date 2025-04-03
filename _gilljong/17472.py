from sys import stdin as s
from collections import deque, defaultdict
s = open('txt/17472.txt', 'r')

N,M = map(int, s.readline().split())

grid = [list(map(int, s.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# BFS로 섬의 위치를 파악
def bfs(i,j,island_n):
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    grid[i][j] = island_n

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and grid[nx][ny] >= 1:
                visited[nx][ny] = 1
                grid[nx][ny] = island_n
                q.append([nx,ny])

island_n = 1

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j,island_n)
            island_n += 1

# 4방향 접근 후 간선 정보 + 비용 반환
def find_left(x,y,k,n,c):
    global distance
    if grid[x][y] != 0 and grid[x][y] != n:
        if c > 2:
            distance.add((n,grid[x][y], c-1)) # 도착 지점과 거리
        return
    nx = x + dx[k]
    ny = y + dy[k]
    if 0<= nx < N and 0 <= ny < M and grid[nx][ny] != n: # 가장자리만 가능하게 구현
        find_left(nx,ny,k,n,c+1)

distance = set()

for i in range(N):
    for j in range(M):
        if grid[i][j] >= 1:
            for k in range(4):
                find_left(i,j,k,grid[i][j],0)

# 최소 신장트리 알고리즘
distance = sorted(list(distance), key = lambda x : x[2])

parent = [0] * (island_n) # 섬의 개수 고려함
answer = 0
visited = set()

for i in range(island_n):
    parent[i] = i

def find_parents(x): #부모, 자식
    if parent[x] != x: # 만약 부모와 자식이 같지 않다면 ?
        parent[x] = find_parents(parent[x])
    return parent[x]

def union(x,y,c):
    global answer
    a = find_parents(x)
    b = find_parents(y)

    visited.add(x) # 방문처리
    visited.add(y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

    answer += c

for item in distance:
    x, y, c = item
    if find_parents(x) != find_parents(y): # 부모의 정점이 다르다면 ?
        union(x,y,c)

is_done = set() # 최소 신장트리로 접근한 부모노드를 순회하면서 모두 연결되었는지 확인
for i in range(1, len(parent)):
    p = find_parents(i)
    is_done.add(p)

if len(is_done) > 1: #만약 모두 연결이 안됐을 경우
    print(-1)
else:
    print(answer)