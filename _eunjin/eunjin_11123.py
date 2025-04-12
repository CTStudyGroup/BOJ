from collections import deque

# bfs로 연결 요소의 개수 찾는 문제
T = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(h, w, matrix):
    visited = [[False] * w for _ in range(h)]
    ret = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '#' and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    y, x = q.popleft()

                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]

                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and matrix[ny][nx] == '#':
                            q.append((ny, nx))
                            visited[ny][nx] = True
                ret += 1
    return ret


for t in range(T):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    print(bfs(H, W, matrix))

