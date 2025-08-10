from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

# 일단 bfs탐색하면서 방문한 1의 개수를 같이 큐에 넘기기
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
q = deque()
q.append((0, 0, 1, 0))  # y, x, depth, cnt
visited[0][0][0] = True
answer = -1

while q:
    y, x, depth, cnt = q.popleft()

    if y == N - 1 and x == M - 1:
        answer = depth
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue

        if matrix[ny][nx] == "1":
            if cnt + 1 > K:  # 더이상 벽 부수기 불가
                continue
            if not visited[ny][nx][cnt + 1]:
                q.append((ny, nx, depth + 1, cnt + 1))
                visited[ny][nx][cnt + 1] = True
        else:
            if not visited[ny][nx][cnt]:
                q.append((ny, nx, depth + 1, cnt))
                visited[ny][nx][cnt] = True

print(answer)
