import sys
input = sys.stdin.readline

T = int(input())

# 11! = 39916800, 각 선수마다 최대 5개 경우의 수이므로 실제 이거보다 작음
# 0~10까지의 순열 중 능력치의 합 최댓값 찾기
# 백트래킹

def backtracking(i):
    global answer
    if i == 11:
        point = 0
        for k in range(11):
            point += matrix[k][selected[k]]

        answer = max(answer, point)
        return

    for j in range(11):
        if matrix[i][j] and not used[j]:
            selected[i] = j
            used[j] = True
            backtracking(i + 1)
            used[j] = False


for _ in range(T):
    answer = 0
    selected = [-1] * 11  # 각 선수마다 선택한 포지션 인덱스
    used = [False] * 11  # 포지션마다 현재 사용 여부
    matrix = [list(map(int, input().split())) for _ in range(11)]
    backtracking(0)

    print(answer)
