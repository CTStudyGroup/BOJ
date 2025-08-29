import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 구름 d 방향으로 s칸 이동
def move_cloud(d, s):
    global clouds
    temp = []
    for cy, cx in clouds:
        ny = (cy + dy[d] * s) % N
        nx = (cx + dx[d] * s) % N
        temp.append((ny, nx))

    clouds = temp


# 비 내리고 구름 삭제, 비 내린 좌표 리스트 반환
def rain_drop():
    global clouds
    ret = []
    for y, x in clouds:
        matrix[y][x] += 1
        ret.append((y, x))
        rain_visited[y][x] = True
    clouds = []
    return ret


ry = [-1, -1, 1, 1]
rx = [-1, 1, -1, 1]

# 비 내린 칸마다 물복사버그
# 대각선 방향으로 1칸 이내에 물이 있는 바구니 수만큼 (r,c)의 물의 양 증가
def copy_water(rains):
    for y, x in rains:
        cnt = 0
        for i in range(4):  # 대각선 인접 네 칸에 물이 있는 바구니 수 세기
            ny, nx = y + ry[i], x + rx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[ny][nx]:
                    cnt += 1
        matrix[y][x] += cnt  # 물 증가


# 구름 생성, 이전에 구름 삭제되었던 좌표는 생성X
# 물의 양이 2 이상인 모든 칸에 구름 생성, 물 양 -2
def create_clouds(rains):
    for y in range(N):
        for x in range(N):
            if rain_visited[y][x]:  # 이전에 구름 삭제되었던 좌표
                rain_visited[y][x] = False
                continue
            if matrix[y][x] >= 2:
                clouds.append((y, x))
                matrix[y][x] -= 2


clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]  # 비구름 시작
rain_visited = [[False] * N for _ in range(N)]

for _ in range(M):
    d, s = map(int, input().split())
    move_cloud(d, s)
    rains = rain_drop()
    copy_water(rains)
    create_clouds(rains)

answer = 0
for row in matrix:
    answer += sum(row)

print(answer)
