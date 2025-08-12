from itertools import product
import copy
N, M = map(int, input().split())
origin_matrix = [list(input()) for _ in range(N)]

# 구멍 좌표 구하기
hole_y, hole_x = -1, -1
sry, srx, sby, sbx = -1, -1, -1, -1
for y in range(N):
    for x in range(M):
        if origin_matrix[y][x] == "O":
            hole_y, hole_x = y, x
        elif origin_matrix[y][x] == "R":
            sry, srx = y, x
        elif origin_matrix[y][x] == "B":
            sby, sbx = y, x

def vert(ry, rx, by, bx, d):  # d: -1(상), +1(하)
    red_fin, blue_fin = False, False

    curr_y = ry
    while True:
        ny = curr_y + d
        if matrix[ny][rx] == ".":
            curr_y += d
            continue
        elif matrix[ny][rx] == "O":
            red_fin = True
            curr_y += d
            break
        elif matrix[ny][rx] == "B":  # 이동 중에 B를 만난 경우, B의 최종 y좌표-d로 확정됨
            break
        elif matrix[ny][rx] == "#":
            red_fin = True
            break
    if red_fin:
        ry = curr_y

    curr_y = by
    while True:
        ny = curr_y + d
        if matrix[ny][bx] == ".":
            curr_y += d
            continue
        elif matrix[ny][bx] == "O":
            blue_fin = True
            curr_y += d
            break
        elif matrix[ny][bx] == "R":  # 이동 중에 R를 만난 경우, R의 최종 y좌표-d로 확정됨
            break
        elif matrix[ny][bx] == "#":
            blue_fin = True
            break
    if blue_fin:
        by = curr_y

    if not red_fin and blue_fin:
        if by == hole_y and bx == hole_x:
            ry = by
        else:
            ry = by - d


    if not blue_fin and red_fin:
        if ry == hole_y and rx == hole_x:
            by = ry
        else:
            by = ry - d

    return ry, rx, by, bx

def horz(ry, rx, by, bx, d):  # d: +1(우), -1(좌)
    red_fin, blue_fin = False, False

    curr_x = rx
    while True:
        nx = curr_x + d
        if matrix[ry][nx] == ".":
            curr_x += d
            continue
        elif matrix[ry][nx] == "O":
            red_fin = True
            curr_x += d
            break
        elif matrix[ry][nx] == "B":  # 이동 중에 B를 만난 경우, B의 최종 y좌표-d로 확정됨
            break
        elif matrix[ry][nx] == "#":
            red_fin = True
            break
    if red_fin:
        rx = curr_x

    curr_x = bx
    while True:
        nx = curr_x + d
        if matrix[by][nx] == ".":
            curr_x += d
            continue
        elif matrix[by][nx] == "O":
            blue_fin = True
            curr_x += d
            break
        elif matrix[by][nx] == "R":  # 이동 중에 R를 만난 경우, R의 최종 y좌표-d로 확정됨
            break
        elif matrix[by][nx] == "#":
            blue_fin = True
            break
    if blue_fin:
        bx = curr_x

    if not red_fin and blue_fin:
        if by == hole_y and bx == hole_x:
            rx = bx
        else:
            rx = bx - d

    if not blue_fin and red_fin:
        if ry == hole_y and rx == hole_x:
            bx = rx
        else:
            bx = rx - d

    return ry, rx, by, bx

# 상하좌우 방향으로 기울이기, 각 구슬의 좌표 반환
# matrix 업데이트
def tilt(red_y, red_x, blue_y, blue_x, cmd):
    # # 빨간색, 파란색 구슬 좌표 찾기
    # red_y, red_x = -1, -1
    # blue_y, blue_x = -1, -1
    # for y in range(1, N - 1):
    #     for x in range(1, M - 1):
    #         if matrix[y][x] == "R":
    #             red_y, red_x = y, x
    #         elif matrix[y][x] == "B":
    #             blue_y, blue_x = y, x

    nry, nrx, nby, nbx = -1, -1, -1, -1

    if cmd == 0:  # 위쪽 기울이기
        nry, nrx, nby, nbx = vert(red_y, red_x, blue_y, blue_x, -1)
    elif cmd == 1:  # 아래쪽 기울이기
        nry, nrx, nby, nbx = vert(red_y, red_x, blue_y, blue_x, 1)
    elif cmd == 2:  # 왼쪽 기울이기
        nry, nrx, nby, nbx = horz(red_y, red_x, blue_y, blue_x, -1)
    else:
        nry, nrx, nby, nbx = horz(red_y, red_x, blue_y, blue_x, 1)

    matrix[red_y][red_x] = "."
    matrix[blue_y][blue_x] = "."

    matrix[nry][nrx] = "R"
    matrix[nby][nbx] = "B"

    return nry, nrx, nby, nbx


# matrix = copy.deepcopy(origin_matrix)
# # print(tilt(0))
# # print(tilt(1))
# print(tilt(2))


# 10번의 실행 횟수 중 4가지 커맨드(상,하,좌,우) 중 택 1 하는 모든 경우의 수 탐색
# 4^10 = 1048576
# 236196
total_comb = []
arr = []

def bt(n):
    if len(arr) == 10:
        total_comb.append(arr[:])
        return

    for i in range(4):
        if i != n:
            arr.append(i)
            bt(i)
            arr.pop()

for i in range(4):
    bt(i)

# total_comb = [[2, 1, 3, 1, 2, 0]]

for comb in total_comb:
    # print("comb:", comb)
    matrix = copy.deepcopy(origin_matrix)
    ry, rx, by, bx = sry, srx, sby, sbx
    for i in range(len(comb)):
        cmd = comb[i]
        # 방향에 맞게 기울였을 때의 각 좌표 구하기
        ry, rx, by, bx = tilt(ry, rx, by, bx, cmd)
        # print("cmd:", cmd, ", red:", ry, rx, ", blue:", by, bx)

        if ry == by and rx == bx and ry == hole_y and rx == hole_x:  # 두 구슬 동시에 구멍에 빠짐
            break  # 다음 comb 조합 탐색

        if ry == hole_y and rx == hole_x:  # 빨간 구슬만 구멍에 빠진 경우 1 출력 후 종료
            print(1)
            exit()
