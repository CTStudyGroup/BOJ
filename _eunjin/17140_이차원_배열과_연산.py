from collections import defaultdict

R, C, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

def print_matrix(mat):
    print("-----")
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

# 연산
def calc():
    global matrix
    temp_matrix = []
    maxR = 0

    for r in range(len(matrix)):
        # 수 등장 횟수 계산
        _dict = defaultdict(int)
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:  # 0은 무시
                continue
            _dict[matrix[r][c]] += 1

        # 정렬: 등장 횟수가 작은 것 부터, 같은 등장 횟수인 경우 수가 작은 것 부터
        arr = []
        for n, c in _dict.items():
            arr.append((n, c))  # 수, 등장 횟수
        arr = sorted(arr, key=lambda x: (x[1], x[0]))

        # 새 행 생성
        new_row = []
        for elem in arr:
            new_row.append(elem[0])
            new_row.append(elem[1])

        if len(new_row) > 100:  # 처음 100개 제외 나머지 버림
            new_row = new_row[:100]

        maxR = max(maxR, len(new_row))  # 최대 행 크기 갱신
        temp_matrix.append(new_row)  # 임시 행렬에 해당 행 추가

    # 최대 행 크기 기준으로 0 채우기
    for r in range(len(temp_matrix)):
        if len(temp_matrix[r]) == maxR:
            continue
        for _ in range(len(temp_matrix[r]), maxR):
            temp_matrix[r].append(0)

    matrix = temp_matrix

# 행 <-> 열 변환
def reverse():
    global matrix
    temp_matrix = [[] for _ in range(len(matrix[0]))]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            temp_matrix[c].append(matrix[r][c])

    matrix = temp_matrix


T = 0
while T <= 100:
    # print("trial:", T)
    rlen = len(matrix)
    clen = len(matrix[0])

    if R - 1 < rlen and C - 1 < clen:
        if matrix[R - 1][C - 1] == K:
            print(T)
            exit()

    if rlen >= clen:  # R연산
        calc()
    else:  # C연산
        reverse()
        calc()
        reverse()

    # print_matrix(matrix)
    T += 1

print(-1)
