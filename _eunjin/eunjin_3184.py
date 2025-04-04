from collections import deque

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

# o, v의 개수 세기
O = 0
V = 0

for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'o':
            O += 1
        elif matrix[r][c] == 'v':
            V += 1

# bfs로 영역 탐색하면서 각 영역별 o와 v의 개수 세기
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if visited[r][c] or matrix[r][c] == '#':
            continue

        vn = 0
        on = 0
        q = deque()
        q.append((r, c))
        visited[r][c] = True

        while q:
            y, x = q.popleft()
            if matrix[y][x] == 'o':
                on += 1
            elif matrix[y][x] == 'v':
                vn += 1

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                    if matrix[ny][nx] != '#':
                        q.append((ny, nx))
                        visited[ny][nx] = True

        if on > vn:
            V -= vn
        else:
            O -= on

print(O, V)
