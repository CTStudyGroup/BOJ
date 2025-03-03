import copy
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for y in range(N):
    for x in range(M):
        if 1 <= matrix[y][x] <= 5:
            cctvs.append((matrix[y][x], y, x))  # cctv 번호, y,x

# 0, 90, 180, 270도 회전
cctv1 = [[0], [1], [2], [3]]  # 오,아,왼,위
cctv2 = [[0, 2],  # 위,아
         [1, 3]]  # 오,왼
cctv3 = [[0, 1],  # 위,오
         [1, 2],  # 오,아
         [2, 3],  # 아,왼
         [3, 0]]  # 왼,위
cctv4 = [[0, 1, 2],  # 위,오,아
         [1, 2, 3],  # 오,아,왼
         [2, 3, 0],  # 아,왼,위
         [3, 0, 1]]  # 왼,위,오
cctv5 = [[0, 1, 2, 3]]  # 위,왼,오,아

d = [[], cctv1, cctv2, cctv3, cctv4, cctv5]

# 상, 우, 하, 좌
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def watch(matrix, dirr, y, x):
    # print("watch called:", dirr, y, x)
    for i in dirr:
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M:  # 범위 벗어난 경우
                break

            if matrix[ny][nx] == 6:  # 벽 만난 경우
                break

            if matrix[ny][nx] == 0:  # 감시 처리
                matrix[ny][nx] = -1

def backtracking(depth, matrix):
    # print("backtracking:", depth)
    global answer
    if depth == len(cctvs):  # 탐색 종료
        cnt = 0
        for i in range(N):  # 사각지대 개수 세기
            cnt += matrix[i].count(0)
        answer = min(answer, cnt)
        return

    temp = copy.deepcopy(matrix)  # matrix 복사
    num, y, x = cctvs[depth]  # 탐색할 cctv

    for i in d[num]:
        watch(temp, i, y, x)  # cctv 감시
        backtracking(depth + 1, temp)  # 다음 cctv 탐색
        temp = copy.deepcopy(matrix)


answer = float('inf')
backtracking(0, matrix)  # 0번째 cctv부터 탐색 시작
print(answer)

