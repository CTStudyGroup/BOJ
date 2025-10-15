from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# matrix[y][x]: [0,0,0,0], 남동북서 순서로 벽이 있는지 여부
matrix = [[[] for _ in range(N)] for _ in range(M)]

for m in range(M):
    row = list(map(int, input().split()))
    for n in range(len(row)):
        st = bin(row[n])[2:]
        st = "0" * (4 - len(st)) + st  # 길이 4로 통일
        matrix[m][n] = list(map(int, st))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx, k):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    ret = 0

    while q:
        y, x = q.popleft()
        area_matrix[y][x] = k
        ret += 1

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue

            if not visited[ny][nx] and not matrix[y][x][i]:  # 벽이 없을 때에만 다음 탐색
                q.append((ny, nx))
                visited[ny][nx] = True
    return ret

visited = [[False] * N for _ in range(M)]
total_connected = 0
largest = 0

area_matrix = [[-1] * N for _ in range(M)]  # 영역 구분 matrix
area_size = []  # 각 영역별 연결된 노드의 개수

for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            cnt = bfs(y, x, total_connected)
            largest = max(largest, cnt)
            area_size.append(cnt)  # 해당 영역의 크기 초기화
            total_connected += 1


# 연결된 영역마다 고유 번호 부여
# 0 0 1 1 2 2 2
# 0 0 0 1 2 3 2
# 0 0 0 4 2 4 2
# 0 4 4 4 4 4 2

# 인접한 노드의 영역 번호가 다르면, 거기에 벽이 있는 것임
adj_sum = [[0] * len(area_size) for _ in range(len(area_size))]  # 각 영역끼리 연결되었을 때 만들어지는 영역 크기

# 전체 matrix 모든 좌표마다 돌면서 인접 영역와의 크기 합 구하기
for y in range(M):
    for x in range(N):
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue

            curr = area_matrix[y][x]
            adj = area_matrix[ny][nx]
            if adj == curr:  # 같은 영역
                adj_sum[curr][adj] = area_size[curr]
                continue

            if adj_sum[curr][adj] > 0:  # 이미 계산된 영역
                continue

            adj_sum[curr][adj] = area_size[curr] + area_size[adj]
            adj_sum[adj][curr] = area_size[curr] + area_size[adj]

answer = 0
for row in adj_sum:
    answer = max(answer, max(row))

print(total_connected)  # 연결 요소의 개수
print(largest)  # 연결 요소 내 최대 노드 개수
print(answer)  # 벽 하나 제거했을 때의 연결 요소 내 최대 노드 개수

