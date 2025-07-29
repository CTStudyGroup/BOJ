from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
start_y, start_x, start_d = map(int, input().split())
target_y, target_x, target_d = map(int, input().split())

dd = [0, 0, 2, 1, 3]  # 0123: 동남서북
start_d, target_d = dd[start_d], dd[target_d]

# 주어진 좌표까지의 최단 경로 구하기
# 그 경로로 이동하면서 명령 횟수 세기

# 그냥 bfs로 탐색하면서 명령 횟수까지 같이 구해야할 듯
# visited 3차원으로 두고 거기에 명령 횟수 저장

dy = [0, 1, 0, -1]  # 동남서북
dx = [1, 0, -1, 0]

visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]

q = deque()
q.append((start_y - 1, start_x - 1, start_d))  # y, x, d

while q:
    cy, cx, cd = q.popleft()
    curr = visited[cy][cx][cd]

    if cy == target_y - 1 and cx == target_x - 1 and cd == target_d:
        print(curr)
        break

    # i칸 이동, 1~3칸씩 이동 각각을 큐에 담아야 함
    for i in range(1, 4):
        ny = cy + dy[cd] * i
        nx = cx + dx[cd] * i
        if ny < 0 or ny >= M or nx < 0 or nx >= N:  # 그 이상 이동 볼가
            break
        if matrix[ny][nx]:
            break
        if not visited[ny][nx][cd]:
            visited[ny][nx][cd] = curr + 1
            q.append((ny, nx, cd))

    # 회전
    if not visited[cy][cx][(cd - 1) % 4]:
        visited[cy][cx][(cd - 1) % 4] = curr + 1
        q.append((cy, cx, (cd - 1) % 4))

    if not visited[cy][cx][(cd + 1) % 4]:
        visited[cy][cx][(cd + 1) % 4] = curr + 1
        q.append((cy, cx, (cd + 1) % 4))

