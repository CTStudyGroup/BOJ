from sys import stdin as s
from collections import deque,defaultdict
s = open('txt/1783.txt', 'r')

R, C = map(int,s.readline().split())

grid = [list(s.readline().strip()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]

dx = [-1,0,1,0] #방향 변수
dy = [0,1,0,-1]

def bfs(i,j):
    global o,v
    cnt = defaultdict(int) #딕셔너리로 매번 o, v값을 구해줌

    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    cnt[grid[i][j]] += 1

    while q:
        x,y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and grid[nx][ny] != '#':
                visited[nx][ny] = 1
                cnt[grid[nx][ny]] += 1
                q.append([nx,ny])

    if cnt['o'] > cnt['v']: #만약 양이 늑대보다 크다면 ?
        cnt['v'] = 0
    else: # 만약 양이 늑대와 같거나 작다면
        cnt['o'] = 0
    o += cnt['o']
    v += cnt['v']

o,v = 0, 0

for i in range(R):
    for j in range(C):
        if (grid[i][j] == 'o' or grid[i][j] == 'v') and visited[i][j] == 0:
            bfs(i,j)

print(o,v)

# 25m 15s