from collections import deque

# 입력 받기
M, N, H = map(int, input().split())

matrix = [[] for _ in range(H)]
for h in range(H):
    for n in range(N):
        matrix[h].append(list(map(int, input().split())))

# 저장될 때부터 모든 토마토가 익어 있는 상태이면 0 출력
cnt = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if matrix[z][y][x] == 0:
                cnt += 1

if(cnt == 0):
    print(0)
    exit()


INF = int(1e12)

q = deque()
time = [[[INF] * M for _ in range(N)] for _ in range(H)]  # 소요 시간 배열 초기화

for z in range(H):
    for y in range(N):
        for x in range(M):
            if matrix[z][y][x] == 1:
                q.append((z, y, x))
                time[z][y][x] = 0
            if matrix[z][y][x] == -1:
                time[z][y][x] = 0

while q:
    z, y, x = q.popleft()

    nexts = [(z, y-1, x), (z, y, x-1), (z, y+1, x),
             (z, y, x+1), (z+1, y, x), (z-1, y, x)]  # 다음으로 갈 수 있는 노드 후보 리스트

    for nz, ny, nx in nexts:
        if not (0 <= ny < N and 0 <= nx < M and 0 <= nz < H):  # index 범위가 주어진 범위를 초과하는 경우
            continue
        if time[nz][ny][nx] <= time[z][y][x]+1:  # 다음 노드를 가는 더 짧은 경로가 이미 존재하는 경우
            continue
        if matrix[nz][ny][nx] == -1:  # 다음 노드에 토마토가 없는 경우
            continue
        q.append((nz, ny, nx))
        time[nz][ny][nx] = time[z][y][x]+1

ans = -1

for z in range(H):
    for y in range(N):
        for x in range(M):
            ans = max(ans, time[z][y][x])

print(ans if ans != INF else -1)
