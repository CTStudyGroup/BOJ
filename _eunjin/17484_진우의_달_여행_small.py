import sys

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 윗 행까지 이동에서 사용한 연료에 현재 칸의 연료 더해주면서 밑으로 내려가기
# dp
INF = sys.maxsize
dp = [[[INF, INF, INF] for _ in range(M)] for _ in range(N)]  # l,u,r

for i in range(M):
    dp[0][i] = [matrix[0][i]] * 3

for i in range(1, N):
    for j in range(M):
        # left
        if j > 0:
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + matrix[i][j]
        # right
        if j < M - 1:
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + matrix[i][j]

        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + matrix[i][j]

# print('\n'.join(' '.join(map(str, row)) for row in dp))

answer = INF
for arr in dp[N - 1]:
    answer = min(answer, min(arr))

print(answer)
