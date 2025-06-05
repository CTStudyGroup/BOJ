from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 외부 영역 기준으로 bfs해서 경계선의 치즈 모두 찾아내기
# 외부 영역을 어떻게 판별할 수 있는지
# 해당 영역이 상하좌우로 치즈와 인접해있는지 여부로 판단?
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def find():
    visited = [[False] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if matrix[y][x] and not visited[y][x]:
                # bfs
                temp = []

                q = deque()
                visited[y][x] = True
                q.append((y, x))

                while q:
                    cy, cx = q.popleft()

                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]
                        if ny < 0 or ny >= N or nx < 0 or nx >= M:
                            continue

                        if matrix[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx))


def valid():
    for row in matrix:
        if sum(row) > 0:
            return False
    return True

T = 0
# while valid():
#     # 외부 영역 찾기
#     # 치즈 녹이기
#     T += 1

print(T)
