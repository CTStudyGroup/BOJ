import sys
from collections import deque

N = int(input())

r1, c1, r2, c2 = map(int, input().split())

q = deque()
q.append((r1, c1, 0))
visited = [[0]*N for _ in range(N)]
visited[c1][r1] = 1
d = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]
while q :
  x, y, cnt = q.popleft()
  if x ==r2 and y == c2 :
    print(cnt)
    sys.exit()
  else :
    for dx, dy in d :
      nx, ny = x +dx, y + dy
      if 0<= nx < N and 0<= ny < N :
        if visited[ny][nx] == 0 :
          visited[ny][nx] = 1
          q.append((nx, ny, cnt + 1))
          
print(-1)
