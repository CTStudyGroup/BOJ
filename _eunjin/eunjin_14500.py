# 입력 받기
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# y,x
tetro = [
        [[0, 0, 0, 0], [0, 1, 2, 3]],  # tetro 1
        [[0, 0, 1, 1], [0, 1, 0, 1]],  # tetro 2
        [[0, 1, 2, 2], [0, 0, 0, 1]],  # tetro 3
        [[0, 1, 1, 2], [0, 0, 1, 1]],  # tetro 4
        [[0, 0, 1, 0], [0, 1, 1, 2]]  # tetro 5
]

# 회전, 대칭 도형 추가
tetro.append([[0, 1, 2, 3], [0, 0, 0, 0]])  # tetro 1 회전
tetro.append([[1, 1, 1, 0], [0, 1, 2, 2]])  # tetro 3 회전
tetro.append([[0, 0, 1, 2], [0, 1, 1, 1]])  # tetro 3 회전
tetro.append([[0, 0, 0, 1], [0, 1, 2, 0]])  # tetro 3 회전
tetro.append([[0, 1, 2, 2], [1, 1, 1, 0]])  # tetro 3 대칭
tetro.append([[0, 1, 1, 1], [0, 0, 1, 2]])  # tetro 3 대칭
tetro.append([[0, 1, 2, 0], [0, 0, 0, 1]])  # tetro 3 대칭
tetro.append([[0, 0, 0, 1], [0, 1, 2, 2]])  # tetro 3 대칭
tetro.append([[1, 1, 0, 0], [0, 1, 1, 2]])  # tetro 4 회전
tetro.append([[0, 1, 1, 2], [1, 1, 0, 0]])  # tetro 4 대칭
tetro.append([[0, 0, 1, 1], [0, 1, 1, 2]])  # tetro 4 대칭
tetro.append([[0, 1, 2, 1], [0, 0, 0, 1]])  # tetro 5 회전
tetro.append([[0, 1, 1, 1], [1, 0, 1, 2]])  # tetro 5 회전
tetro.append([[1, 0, 1, 2], [0, 1, 1, 1]])  # tetro 5 회전


def getNum(y, x):
    global tetro

    num_arr = []

    for t in range(len(tetro)):
        num = 0
        ty = tetro[t][0]
        tx = tetro[t][1]
        for i in range(4):
            ny = y + ty[i]
            nx = x + tx[i]
            if not 0 <= ny < N or not 0 <= nx < M:
                num = 0
                break
            num += matrix[ny][nx]

        num_arr.append(num)
    # print("y:", y, ",x:", x, ",num:", max(num_arr))

    return max(num_arr)


answer = -1
for y in range(N):
    for x in range(M):
        answer = max(answer, getNum(y, x))

print(answer)
