from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

q = deque()
visited[0][0] = True
q.append((0, 0))
while q:
    y, x = q.popleft()

    for dy, dx in [[1, 0], [0, 1]]:
        ny = y + dy * matrix[y][x]
        nx = x + dx * matrix[y][x]
        if 0 <= ny < N and 0 <= nx < N:
            if not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

# for row in visited:
#     for elem in row:
#         print(elem, end=" ")
#     print()

if visited[N - 1][N - 1]:
    print("HaruHaru")
else:
    print("Hing")
