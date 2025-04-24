import sys
import math
input = sys.stdin.readline

# 파이어볼 좌표, 질량, 방향, 속력
# 1번 행은 N번 행과 연결, 1번 열은 N번 열과 연결

# 1. 모든 파이어볼이 자신의 방향으로 자신의 속력만큼 이동
# 이동 중에 같은 칸에 파이어볼 여러개 가능
# 2. 이동이 모두 끝난 후, 2개 이상의 파이어볼이 있는 칸에서 아래 과정 진행
#    2-1. 같은 칸에 있는 파이어볼 모두 하나로 합치기
#    2-2. 파이어볼 4개로 나누기
#         2-2-1. 질량: floor(질량의 합 / 5)
#         2-2-2. 속력: floor(속력의 합 / 합쳐진 파이어볼의 개수)
#         2-2-3. 방향: 합쳐지는 파이어볼의 방향이 모두 홀수 or 모두 홀수: 0,2,4,6  이게 아니면 1,3,5,7
# 3. 질량이 0인 파이어볼은 소멸

N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]
balls = []
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    matrix[r - 1][c - 1].append(i)  # 질량, 속력, 방향
    balls.append([r - 1, c - 1, m, s, d])


def print_matrix():
    print("------------- matirx --------------")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

def print_balls():
    print("==== balls ====")
    for elem in balls:
        print(elem)

# 1번 행은 N번 행과 연결, 1번 열은 N번 열과 연결
def move():
    global matrix
    temp_matrix = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(len(balls)):
        if not balls[i]:  # 삭제된 볼
            continue
        y, x, m, s, d = balls[i]

        ny = (y + dy[d] * s) % N
        nx = (x + dx[d] * s) % N

        # print("ny:", ny, ", nx:", nx, ", matrix:", matrix[ny][nx])

        balls[i][0] = ny
        balls[i][1] = nx

        temp_matrix[ny][nx].append(i)

    matrix = temp_matrix


def check():
    for i in range(N):
        for j in range(N):
            if len(matrix[i][j]) <= 1:
                continue

            # 나누어질 파이어볼의 질량, 속력, 방향 구하기
            cnt = len(matrix[i][j])  # 합쳐진 파이어볼의 개수
            tm = 0
            ts = 0
            first_d = balls[matrix[i][j][0]][4] % 2  # 첫번째 파이어볼의 방향, 1이면 홀수, 0이면 짝수
            d_flag = True

            for b in matrix[i][j]:
                tm += balls[b][2]
                ts += balls[b][3]
                if d_flag:  # 방향이 전부 짝수/홀수 인지 체크
                    curr_d = balls[b][4] % 2
                    if curr_d != first_d:
                        d_flag = False

            tm = math.floor(tm / 5)
            ts = math.floor(ts / cnt)

            # 기존 파이어볼 삭제
            for b in matrix[i][j]:
                balls[b] = []
            matrix[i][j] = []

            # 질량이 0인 파이어볼은 소멸
            if tm == 0:
                continue

            # 4개의 파이어볼 생성
            for k in range(4):
                if d_flag:
                    d = 2 * k
                else:
                    d = 2 * k + 1

                balls.append([i, j, tm, ts, d])

            # matrix 업데이트
            for t in range(4, 0, -1):
                matrix[i][j].append(len(balls) - t)


for _ in range(K):
    move()
    check()

answer = 0
for ball in balls:
    if not ball:
        continue
    answer += ball[2]

print(answer)
