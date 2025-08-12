import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

ry = rx = by = bx = -1
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 'R':
            ry, rx = y, x
            matrix[y][x] = '.'
        elif matrix[y][x] == 'B':
            by, bx = y, x
            matrix[y][x] = '.'

# 상, 하, 좌, 우
dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 벽 or 구멍까지 굴려서 멈춘 위치 좌표, 구멍에 빠졌는지 여부, 이동거리 반환
def move(y, x, dy, dx):
    dist = 0
    while True:
        ny, nx = y + dy, x + dx
        if matrix[ny][nx] == '#':
            return y, x, False, dist
        if matrix[ny][nx] == 'O':
            return ny, nx, True, dist + 1
        y, x = ny, nx
        dist += 1

def bfs(ry, rx, by, bx):
    q = deque()
    q.append((ry, rx, by, bx, 0))
    visited = set()
    visited.add((ry, rx, by, bx))

    while q:
        ryy, rxx, byy, bxx, d = q.popleft()
        if d >= 10:   # 10번 이내만 허용
            continue

        for dy, dx in dd:  # 4가지 방향에 대해 굴리는 경우의 수 탐색
            # 어느 구슬을 먼저 굴릴지 결정
            # 같은 행/열에 있고 이동 방향으로 앞선 구슬을 먼저 굴린다.
            first_red = True
            if dy != 0:  # 상하 기울이기
                if rxx == bxx:  # 같은 열에 있는 경우
                    if dy == -1:  # 위로
                        first_red = (ryy < byy)
                    else:         # 아래로
                        first_red = (ryy > byy)
            else:  # 좌우 기울이기
                if ryy == byy:  # 같은 행에 있는 경우
                    if dx == -1:  # 왼쪽
                        first_red = (rxx < bxx)
                    else:         # 오른쪽
                        first_red = (rxx > bxx)

            if first_red:
                nry, nrx, r_hole, rdist = move(ryy, rxx, dy, dx)
                nby, nbx, b_hole, bdist = move(byy, bxx, dy, dx)
            else:
                nby, nbx, b_hole, bdist = move(byy, bxx, dy, dx)
                nry, nrx, r_hole, rdist = move(ryy, rxx, dy, dx)

            # 파란 구슬 빠진 경우 해당 조합 실패
            if b_hole:
                continue
            # 빨간 구슬 빠진 경우 성공
            if r_hole:
                return 1

            # 같은 칸에 멈추면 더 많이 움직인 쪽을 한 칸 뒤로
            if nry == nby and nrx == nbx:
                if rdist > bdist:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            state = (nry, nrx, nby, nbx)
            if state not in visited:
                visited.add(state)
                q.append((nry, nrx, nby, nbx, d + 1))

    return 0

print(bfs(ry, rx, by, bx))
