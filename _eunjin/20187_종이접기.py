K = int(input())
cmd = list(input().split())
H = int(input())
matrix = [[H]]

# cmd를 뒤에서부터 역연산 수행하면서 구멍 위치 추가하기

# D, U, R, L
CMD_MAP = {"D": 0, "U": 1, "R": 2, "L": 3}

# 종이 폈을 때 복사될 구멍 위치
dd = [2, 3, 0, 1]
du = [2, 3, 0, 1]
dr = [1, 0, 3, 2]
dl = [1, 0, 3, 2]
reverse = [dd, du, dr, dl]

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

# 주어진 c의 역연산 수행
def func(c):
    global matrix
    cidx = CMD_MAP[c]
    temp_matrix = []
    R = len(matrix)
    C = len(matrix[0])

    if cidx == 0:  # 위로 펴기
        temp_matrix = [[] for _ in range(2 * R)]  # 행을 2배로 키우기

        # 위쪽 반에 구멍 위치 추가
        for y in range(R):
            temp_row = []
            for x in range(C):
                temp_row.append(reverse[cidx][matrix[R - y - 1][x]])
            temp_matrix[y] = temp_row[:]

        # 아래쪽 반에 기존 구멍 복사
        for y in range(R, 2 * R):
            temp_matrix[y] = matrix[R - y][:]

    elif cidx == 1:  # 아래로 펴기
        temp_matrix = [[] for _ in range(2 * R)]  # 행을 2배로 키우기

        # 위쪽 반에 기존 구멍 복사
        for y in range(R):
            temp_matrix[y] = matrix[y][:]

        # 아래쪽 반에 구멍 위치 추가
        for y in range(R, 2 * R):
            temp_row = []
            for x in range(C):
                temp_row.append(reverse[cidx][matrix[R - y - 1][x]])
            temp_matrix[y] = temp_row[:]

    elif cidx == 2:  # 왼쪽으로 펴기
        temp_matrix = [[] for _ in range(R)]  # 행 크기 그대로 설정

        for y in range(R):
            for x in range(2 * C):
                if x < C:  # 왼쪽 반에 구멍 위치 추가
                    temp_matrix[y].append(reverse[cidx][matrix[y][C - x - 1]])
                else:  # 오른쪽 반에 기존 구멍 복사
                    temp_matrix[y].append(matrix[y][x - C])

    else:  # 오른쪽으로 펴기
        temp_matrix = [[] for _ in range(R)]  # 행 크기 그대로 설정
        for y in range(R):
            for x in range(2 * C):
                if x < C:  # 왼쪽 반에 기존 구멍 복사
                    temp_matrix[y].append(matrix[y][x])
                else:  # 오른쪽 반에 구멍 위치 추가
                    temp_matrix[y].append(reverse[cidx][matrix[y][2 * C - x - 1]])

    matrix = temp_matrix

cmd = cmd[::-1]
for c in cmd:
    func(c)

print_matrix(matrix)
