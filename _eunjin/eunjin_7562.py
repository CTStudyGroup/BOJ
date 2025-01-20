from collections import deque
T = int(input())

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(start_y, start_x, end_y, end_x, l):
    q = deque()
    visited = [[False]*l for _ in range(l)]
    q.append((start_y, start_x, 0))
    visited[start_y][start_x] = True

    while q:
        y, x, d = q.popleft()
        # print("y:", y, ", x:", x, ", d:", d)

        if y == end_y and x == end_x:
            return d

        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny >= 0 and ny < l and nx >= 0 and nx < l:
                if visited[ny][nx]:
                    continue
                q.append((ny, nx, d+1))
                visited[ny][nx] = True


for _ in range(T):
    L = int(input())
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())
    print(bfs(start_y, start_x, end_y, end_x, L))
