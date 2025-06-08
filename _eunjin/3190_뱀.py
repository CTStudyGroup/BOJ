from collections import deque

N = int(input())
K = int(input())

matrix = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    matrix[y - 1][x - 1] = 1

cmd = deque()
L = int(input())
for _ in range(L):
    x, c = input().split()
    x = int(x)
    cmd.append((x, c))

rd = [1, 2, 3, 0]
ld = [3, 0, 1, 2]
dy = [-1, 0, 1, 0]  # 상,우,하,좌
dx = [0, 1, 0, -1]

def print_matrix():
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

def turn(c):
    global d
    if c == "L":
        d = ld[d]
    else:
        d = rd[d]

def move():
    hy, hx = snake[0]
    ny, nx = hy + dy[d], hx + dx[d]

    if ny < 0 or ny >= N or nx < 0 or nx >= N:
        return False
    elif matrix[ny][nx] == -1:
        return False

    snake.appendleft((ny, nx))  # head 추가

    if matrix[ny][nx] == 0:  # 사과가 없으면
        ty, tx = snake.pop()
        matrix[ty][tx] = 0  # 꼬리 삭제

    matrix[ny][nx] = -1

    # print_matrix()
    return True

d = 1  # 0,1,2,3 처음 방향은 오른쪽
matrix[0][0] = -1
snake = deque()
snake.append((0, 0))

T = 1
while True:
    if not move():
        break

    if cmd:
        if cmd[0][0] == T:
            turn(cmd.popleft()[1])

    T += 1


print(T)

