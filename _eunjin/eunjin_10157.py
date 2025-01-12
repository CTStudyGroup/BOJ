C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
    exit()

matrix = [[0 for _ in range(C)] for _ in range(R)]

# 1 22 21 20 19 18 17
# 2 23 36 35 34 33 16
# 3 24 37 42 41 32 15
# 4 25 38 39 40 31 15
# 5 26 27 28 29 30 14
# 6 7 8 9 10 11 12 13


def down(y, x):
    n = matrix[y][x]
    y_idx = y+1
    x_idx = x

    while(y_idx < R and matrix[y_idx][x_idx] == 0):
        matrix[y_idx][x_idx] = n+1
        n += 1
        y_idx += 1

    isNext = True if(matrix[y_idx-1][x_idx+1] == 0) else False

    return y_idx-1, x_idx, isNext


def right(y, x):
    n = matrix[y][x]
    y_idx = y
    x_idx = x+1
    while(x_idx < C and matrix[y_idx][x_idx] == 0):
        matrix[y_idx][x_idx] = n+1
        n += 1
        x_idx += 1

    isNext = True if(matrix[y_idx-1][x_idx-1] == 0) else False

    return y_idx, x_idx-1, isNext


def up(y, x):
    n = matrix[y][x]
    y_idx = y-1
    x_idx = x
    while(y_idx >= 0 and matrix[y_idx][x_idx] == 0):
        matrix[y_idx][x_idx] = n+1
        n += 1
        y_idx -= 1

    isNext = True if(matrix[y_idx+1][x_idx-1] == 0) else False

    return y_idx+1, x_idx, isNext


def left(y, x):
    n = matrix[y][x]
    y_idx = y
    x_idx = x-1
    while(x_idx >= 0 and matrix[y_idx][x_idx] == 0):
        matrix[y_idx][x_idx] = n+1
        n += 1
        x_idx -= 1

    isNext = True if(matrix[y_idx+1][x_idx+1] == 0) else False

    return y_idx, x_idx+1, isNext


matrix[0][0] = 1

y, x, isNext = 0, 0, True

while(True):
    y, x, isNext = down(y, x)

    if not isNext:
        break

    y, x, isNext = right(y, x)

    if not isNext:
        break

    y, x, isNext = up(y, x)

    if not isNext:
        break

    y, x, isNext = left(y, x)

    if not isNext:
        break


# print(matrix)
for y in range(R):
    for x in range(C):
        if matrix[y][x] == K:
            print(x+1, y+1)
