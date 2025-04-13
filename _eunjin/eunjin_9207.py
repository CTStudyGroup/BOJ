import sys
input = sys.stdin.readline

N = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def move(time):
    global min_cnt, min_move

    pins = []  # 핀의 위치 저장
    for y in range(5):
        for x in range(9):
            if matrix[y][x] == 'o':
                pins.append((y, x))

    if len(pins) < min_cnt:  # 최솟값 갱신
        min_move = time
        min_cnt = len(pins)

    for y, x in pins:  # 각 핀 마다 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny + dy[i] < 5 and 0 <= nx + dx[i] < 9:  # 인접칸의 그 다음칸 범위 확인
                if matrix[ny][nx] == 'o' and matrix[ny + dy[i]][nx + dx[i]] == '.':  # 인접 칸에 핀이 있고 그 넘어서는 빈공간이면
                    matrix[ny][nx] = '.'  # 인접 칸 핀 삭제
                    matrix[ny + dy[i]][nx + dx[i]] = 'o'  # 내 핀 이동
                    matrix[y][x] = '.'  # 내 핀의 원래 위치 삭제

                    move(time + 1)

                    # 핀 이전 상태로 되돌리기
                    matrix[y][x] = 'o'
                    matrix[ny + dy[i]][nx + dx[i]] = '.'
                    matrix[ny][nx] = 'o'


for _ in range(N):
    min_cnt = sys.maxsize
    min_move = sys.maxsize
    matrix = [list(input().rstrip()) for i in range(5)]
    input()
    move(0)
    print(min_cnt, min_move)
