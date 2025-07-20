from collections import deque


def bfs(X, Y, ex, ey) :
    Q = deque()
    Q.append((0,0,0))
    V = set()
    V.add((0,0))
    while Q :
        cx, cy, t = Q.popleft()
        
        if (cx, cy) == (ex, ey) :
            return t
        for nx, ny in [(X, cy), (cx, Y), (0, cy), (cx, 0), (min(cx+cy, X), max(0, cx+cy-X)), (max(0,cx+cy-Y), min(cx+cy, Y))] :
            if (nx, ny) not in V :
                V.add((nx, ny))
                Q.append((nx, ny, t+1))
    return -1
X, Y, ex, ey = map(int, input().split())

result = bfs(X,Y,ex,ey)
print(result)
