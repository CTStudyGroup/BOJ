import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

def divide(y1, x1, y2, x2):
    global answer
    answer += "("
    mid_y = y1 + (y2 - y1) // 2
    mid_x = x1 + (x2 - x1) // 2
    # print("y1:", y1, ", x1:", x1, ", mid_y:", mid_y, ", mid_x:", mid_x, ", y2:", y2, ", x2:", x2)

    # 왼쪽 위
    ch = matrix[y1][x1]
    cont = True
    for y in range(y1, mid_y):
        if not cont:
            break
        for x in range(x1, mid_x):
            if matrix[y][x] != ch:
                cont = False
                break
    if cont:
        answer += ch
    else:
        divide(y1, x1, mid_y, mid_x)

    # 오른쪽 위
    ch = matrix[y1][mid_x]
    cont = True
    for y in range(y1, mid_y):
        if not cont:
            break
        for x in range(mid_x, x2):
            if matrix[y][x] != ch:
                cont = False
                break
    if cont:
        answer += ch
    else:
        divide(y1, mid_x, mid_y, x2)

    # 왼쪽 아래
    ch = matrix[mid_y][x1]
    cont = True
    for y in range(mid_y, y2):
        if not cont:
            break
        for x in range(x1, mid_x):
            if matrix[y][x] != ch:
                cont = False
                break

    if cont:
        answer += ch
    else:
        divide(mid_y, x1, y2, mid_x)

        # 오른쪽 아래
    ch = matrix[mid_y][mid_x]
    cont = True
    for y in range(mid_y, y2):
        if not cont:
            break
        for x in range(mid_x, x2):
            if matrix[y][x] != ch:
                cont = False
                break
    if cont:
        answer += ch
    else:
        divide(mid_y, mid_x, y2, x2)

    answer += ")"


ch = matrix[0][0]
cont = True
for y in range(N):
    if not cont:
        break
    for x in range(N):
        if matrix[y][x] != ch:
            cont = False

if cont:
    print(ch)
else:
    answer = ""
    divide(0, 0, N, N)
    print(answer)
