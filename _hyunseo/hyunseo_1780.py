N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

cnt_min, cnt_zer, cnt_plus = 0, 0, 0

def divide(x, y, size):
    global cnt_min, cnt_zer, cnt_plus
    val = board[x][y]
    same = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != val:
                same = False
                break
        if not same:
            break

    if same:
        if val == -1:
            cnt_min += 1
        elif val == 0:
            cnt_zer += 1
        else:
            cnt_plus += 1
        return
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                nx = x + i * new_size
                ny = y + j * new_size
                divide(nx, ny, new_size)

divide(0, 0, N)

print(cnt_min)
print(cnt_zer)
print(cnt_plus)
