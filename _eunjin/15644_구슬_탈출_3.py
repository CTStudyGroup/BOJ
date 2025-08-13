from collections import deque
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

# 초기 빨간 구슬, 파란 구슬 좌표
ry = rx = by = bx = -1
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 'R':
            ry, rx = y, x
            matrix[y][x] = '.'
        elif matrix[y][x] == 'B':
            by, bx = y, x
            matrix[y][x] = '.'

# 기존 구슬탈출에서 거리, 경로까지 출력해야하는게 차이점인듯?
# 경로 string을 bfs 파라미터로 넘기기?

dd = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]  # 상하좌우

# move함수
# 해당 방향으로 해당 구슬 이동했을 때 도착하는 좌표, 구멍에 빠졌는지 여부, 이동 거리 반환
def move(y, x, dy, dx):
    dist = 0
    while True:
        ny, nx = y + dy, x + dx
        if matrix[ny][nx] == '#':
            return y, x, False, dist
        elif matrix[ny][nx] == "O":
            return ny, nx, True, dist + 1
        y, x = ny, nx
        dist += 1

def bfs(ry, rx, by, bx):
    q = deque()
    q.append((ry, rx, by, bx, 0, ""))  # 빨간 구슬 좌표, 파란 구슬 좌표, depth, 경로string
    visited = set()
    visited.add((ry, rx, by, bx))

    while q:
        cry, crx, cby, cbx, depth, route = q.popleft()

        if depth >= 10:  # 10회 이동까지만 가능
            continue

        for dy, dx, ds in dd:  # 4가지 방향에 대해 굴리는 경우의 수 탐색
            nry, nrx, r_hole, r_dist = move(cry, crx, dy, dx)  # 빨간 구슬 굴리기
            nby, nbx, b_hole, b_dist = move(cby, cbx, dy, dx)  # 파란 구슬 굴리기

            # 파란 구슬 빠진 경우
            if b_hole:
                continue

            # 빨간 구슬 빠진 경우
            if r_hole:
                return depth + 1, route + ds

            # 두 구슬이 동일한 좌표에 도달한 경우, 더 많이 이동한 쪽을 한칸 뒤로 밀기
            if nry == nby and nrx == nbx:
                if r_dist > b_dist:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            state = (nry, nrx, nby, nbx)  # 다음으로 갈 좌표 상태

            if state not in visited:
                q.append((nry, nrx, nby, nbx, depth + 1, route + ds))

    return -1, ''  # 모든 경로 탐색했는데도 종료가 안됐다면 빨간 구슬 빼낼 수 없음

answer = bfs(ry, rx, by, bx)
if answer[0] >= 0:
    print(answer[0])
    print(answer[1])
else:
    print(answer[0])

