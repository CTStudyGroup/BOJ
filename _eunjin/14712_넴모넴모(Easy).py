N, M = map(int, input().split())

# N*M이 최대 25이다...
# 전체 좌표에 대해 네모 올리는 경우/안올리는 경우 탐색 가능 2^25
# 백트래킹

# (y,x) 좌표 기준 왼쪽 위, 위, 왼쪽 모두 네모가 있으면 false 리턴
# 어차피 행 -> 열 순서로 좌표 탐색하므로 오른쪽 or 아래 방향은 신경 쓸 필요 없음
def valid(y, x):
    if y > 0 and x > 0:
        if matrix[y - 1][x] and matrix[y - 1][x - 1] and matrix[y][x - 1]:
            return False
    return True


# 하나의 행을 순차적으로 탐색
def backtracking(y, x):
    global answer
    if y == N - 1 and x == M:  # 모든 행에 대해 탐색 끝남
        answer += 1
        return


    if x == M:  # 해당 행에 대한 모든 열 탐색 끝남, 다음 행 탐색
        x = 0
        y += 1

    # 해당 좌표에 네모 놓는 경우
    # 네모 놓았을 때 2*2 사각형이 만들어지면 안됨
    if valid(y, x):
        matrix[y][x] = 1
        backtracking(y, x + 1)
        matrix[y][x] = 0


    backtracking(y, x + 1)  # 해당 좌표에 네모 안놓는 경우


answer = 0
matrix = [[0] * M for _ in range(N)]
backtracking(0, 0)
print(answer)
