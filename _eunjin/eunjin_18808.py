N, M, K = map(int, input().split())

notebook = [[0]*M for _ in range(N)]


def rotate(sticker):  # 시계방향으로 90도 회전
    r, c = len(sticker), len(sticker[0])
    new = [[0]*r for _ in range(c)]

    for x in range(c):
        for y in range(r-1, -1, -1):
            new[x][r-y-1] = sticker[y][x]

    return new


def able(sticker, start_y, start_x):  # 현재 노트에 붙일 수 있는지 여부 반환
    global notebook, N, M

    r, c = len(sticker), len(sticker[0])

    if r+start_y > N or c+start_x > M:  # 스티커 크기가 노트 범위를 벗어나는 경우
        return False

    for y in range(r):
        for x in range(c):
            if sticker[y][x] == 1 and notebook[y+start_y][x+start_x] == 1:  # 노트에 이미 스티커가 붙여진 경우
                return False
    return True


def attach(sticker, y, x):  # (y,x) 좌표에 스티커 붙이기
    global notebook

    R, C = len(sticker), len(sticker[0])
    for r in range(R):
        for c in range(C):
            if sticker[r][c] == 1:
                notebook[r+y][c+x] = 1


for _ in range(K):
    row, col = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(row)]
    turn = 0
    attached = False
    while turn < 4 and not attached:
        # print("turn:", turn, ", sticker:", sticker)
        # print("notebook:", notebook)

        for curr_y in range(N):
            for curr_x in range(M):
                if able(sticker, curr_y, curr_x):
                    attach(sticker, curr_y, curr_x)
                    attached = True
                    # print("attatched")
                    break
            if attached:
                break

        sticker = rotate(sticker)
        turn += 1

cnt = 0
for row in notebook:
    cnt += sum(row)
print(cnt)
