N, L = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


def slop_possible(y1, x1, y2, x2):  # (y1,x1) ~ (y2,x2)에 경사로를 놓을 수 있는지 여부 반환
    num = matrix[y1][x1]
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if matrix[y][x] != num:
                return False
            if slope[y][x]:
                return False
    return True


answer = 0
slope = [[0]*N for _ in range(N)]

# 가로 방향 탐색
for y in range(N):
    possible = True
    for x in range(N-1):
        if matrix[y][x] < matrix[y][x+1]:  # 높이가 높아지는 경우
            if matrix[y][x+1]-matrix[y][x] > 1:  # 높이 차이가 1이 아닌 경우
                possible = False
                break

            if x-L+1 < 0:  # 경사로가 matrix 범위 벗어나는 경우
                possible = False
                break

            if not slop_possible(y, x-L+1, y, x):  # 뒤에서부터 현재 좌표까지 경사로 놓을 수 있는지
                possible = False
                break

            for i in range(x-L+1, x+1):  # 경사로 놓기
                slope[y][i] = 1
        elif matrix[y][x] > matrix[y][x+1]:  # 높이가 낮아지는 경우
            if matrix[y][x]-matrix[y][x+1] > 1:
                possible = False
                break

            if x+L >= N:  # 경사로가 matrix 범위 벗어나는 경우
                possible = False
                break

            if not slop_possible(y, x+1, y, x+L):
                possible = False
                break

            for i in range(x+1, x+L+1):
                slope[y][i] = 1
    if possible:
        answer += 1
    else:  # slope 초기화
        for j in range(N):
            slope[y][j] = 0


slope = [[0]*N for _ in range(N)]
# 세로 방향 탐색
for x in range(N):
    possible = True
    for y in range(N-1):
        if matrix[y][x] < matrix[y+1][x]:  # 높이가 높아지는 경우
            if matrix[y+1][x]-matrix[y][x] > 1:  # 높이 차이가 1이 아닌 경우
                possible = False
                break

            if y-L+1 < 0:  # 경사로가 matrix 범위 벗어나는 경우
                possible = False
                break

            if not slop_possible(y-L+1, x, y, x):  # 뒤에서부터 현재 좌표까지 경사로 놓을 수 있는지
                possible = False
                break

            for i in range(y-L+1, y+1):  # 경사로 놓기
                slope[i][x] = 1
        elif matrix[y][x] > matrix[y+1][x]:  # 높이가 낮아지는 경우
            if matrix[y][x]-matrix[y+1][x] > 1:
                possible = False
                break

            if y+L >= N:  # 경사로가 matrix 범위 벗어나는 경우
                possible = False
                break

            if not slop_possible(y+1, x, y+L, x):
                possible = False
                break

            for i in range(y+1, y+L+1):
                slope[i][x] = 1
    if possible:
        answer += 1
    else:
        for j in range(N):
            slope[j][x] = 0

print(answer)
