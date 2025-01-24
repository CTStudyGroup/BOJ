from collections import deque

# d: 0(상), 1(우), 2(하), 3(좌)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
rd = [1, 2, 3, 0]
ld = [3, 0, 1, 2]


def rotate(d_input):
    global d
    if d_input == "L":  # 왼쪽으로 90도 회전
        nd = ld[d]
    else:  # 오른쪽으로 90도 회전
        nd = rd[d]
    d = nd


N = int(input())
K = int(input())

matrix = [[0]*N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    matrix[y-1][x-1] = 1

L = int(input())
rotate_list = [[] for _ in range(10001)]
for _ in range(L):
    x, c = input().split()
    rotate_list[int(x)].append(c)

matrix[0][0] = -1
d = 1  # 뱀의 방향
snake = deque()  # 뱀의 좌표 덱
snake.append((0, 0))

for T in range(1, 10001):
    # 머리 좌표 계산
    y, x = snake[0]
    hy = y+dy[d]
    hx = x+dx[d]

    # 벽과 부딪힘 여부
    if hy < 0 or hy >= N or hx < 0 or hx >= N:
        print(T)
        exit()
    # 자기자신과 부딪힘 여부
    if matrix[hy][hx] == -1:
        print(T)
        exit()

    # 머리 좌표 이동
    apple = matrix[hy][hx]  # 사과 존재 여부 저장
    matrix[hy][hx] = -1
    snake.appendleft((hy, hx))

    if not apple:  # 이동한 칸에 사과가 없는 경우
        ty, tx = snake.pop()
        matrix[ty][tx] = 0

    # 방향 전환
    if rotate_list[T]:
        rotate(rotate_list[T][0])
