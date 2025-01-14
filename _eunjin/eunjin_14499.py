N, M, y, x, K = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

command = list(input().split())

dirr = [0, 1, 2, 3, 4, 5, 6]
dice = [0]*7


def east():
    global dirr
    temp = dirr[1]
    dirr[1] = dirr[3]
    dirr[3] = dirr[6]
    dirr[6] = dirr[4]
    dirr[4] = temp


def west():
    global dirr
    temp = dirr[1]
    dirr[1] = dirr[4]
    dirr[4] = dirr[6]
    dirr[6] = dirr[3]
    dirr[3] = temp


def north():
    global dirr
    temp = dirr[1]
    dirr[1] = dirr[2]
    dirr[2] = dirr[6]
    dirr[6] = dirr[5]
    dirr[5] = temp


def south():
    global dirr
    temp = dirr[1]
    dirr[1] = dirr[5]
    dirr[5] = dirr[6]
    dirr[6] = dirr[2]
    dirr[2] = temp


for i in range(K):
    cmd = command[i]
    if cmd == "1":  # east
        if x+1 >= M:
            continue
        x += 1
        east()

    elif cmd == "2":  # west
        if x-1 < 0:
            continue
        x -= 1
        west()

    elif cmd == "3":  # north
        if y-1 < 0:
            continue
        y -= 1
        north()

    else:  # south
        if y+1 >= N:
            continue
        y += 1
        south()
    # print("i:", i, ",cmd:", cmd, "y:", y, ", x:", x)

    bottom = dirr[1]  # 아랫면에 닿아있는 주사위 번호
    if(matrix[y][x] == 0):
        matrix[y][x] = dice[bottom]
    else:
        dice[bottom] = matrix[y][x]
        matrix[y][x] = 0

    top = dirr[6]  # 윗면을 향하고 있는 주사위 번호
    print(dice[top])  # 주사위에 적힌 숫자 출력
