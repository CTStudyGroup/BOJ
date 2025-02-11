from itertools import combinations


def backtracking(depth):
    global cnt

    if depth == 15:
        cnt = 1
        for row in matrix:
            if sum(row) != 0:
                cnt = 0
                break
        return

    g1, g2 = games[depth]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if matrix[g1][x] and matrix[g2][y]:
            matrix[g1][x] -= 1
            matrix[g2][y] -= 1
            backtracking(depth+1)
            matrix[g1][x] += 1
            matrix[g2][y] += 1


answer = []
games = list(combinations(range(6), 2))  # 6팀 중 두 팀을 뽑는 모든 조합

for _ in range(4):
    arr = list(map(int, input().split()))
    matrix = [arr[i:i+3] for i in range(0, 16, 3)]
    cnt = 0
    backtracking(0)
    answer.append(cnt)

print(*answer)
