R, C, M = map(int, input().split())

# 각 좌표에 있는 상어의 [s,d,z] 저장
matrix = [[[] for _ in range(C)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[r-1][c-1].append([s, d, z])


def catch(c):  # 낚시꾼이 상어 잡기
    global R, matrix, total_size
    for y in range(R):
        if matrix[y][c]:
            # print("size add:", matrix[y][c][0][2])

            total_size += matrix[y][c][0][2]  # 잡힌 상어 사이즈 업데이트
            matrix[y][c] = []
            return


def move_shark():  # 상어 이동
    global R, C, matrix
    temp = [[[] for _ in range(C)] for _ in range(R)]  # 이동한 상어 저쟝용 임시 배열
    for r in range(R):
        for c in range(C):
            # print("i:", i, ',r:', r, ",c:", c)

            if matrix[r][c]:
                s, d, z = matrix[r][c][0]
                matrix[r][c] = []

                dist = s  # 이동해야하는 거리
                y, x = r, c
                while dist:
                    # 일단 한 칸 이동

                    y = y+dy[d]
                    x = x+dx[d]
                    if 0 <= y < R and 0 <= x < C:  # 한칸 이동했을 때 유효하면 dis -1
                        dist -= 1
                    else:  # 한칸 이동했을 때 범위 넘어가면 이동한 것 취소, 방향 바꾸기
                        y -= dy[d]
                        x -= dx[d]
                        d = dd[d]  # 방향 전환
                temp[y][x].append([s, d, z])

    # for row in temp:
    #     for col in row:
    #         print(col, end=" ")
    #     print()
    # print("------------------")

    for y in range(R):
        for x in range(C):
            if len(temp[y][x]) >= 1:
                temp[y][x].sort(key=lambda x: x[2], reverse=True)
                s, d, z = temp[y][x][0]
                matrix[y][x] = [[s, d, z]]  # 가장 큰 상어 하나만 남기기

    # for row in matrix:
    #     for col in row:
    #         print(col, end=" ")
    #     print()
    # print("======================")


total_size = 0

dd = [0, 2, 1, 4, 3]  # d의 반대방향 저장
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

for i in range(C):
    catch(i)
    move_shark()


# for row in matrix:
#     for col in row:
#         print(col, end=" ")
#     print()
print(total_size)
