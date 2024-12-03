# 입력 받기
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

# dp 초기화
dp[0][0][1] = 1
for i in range(2, N):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, N):
    for c in range(1, N):
        # 대각선 파이프 추가
        if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
            dp[1][r][c] = dp[0][r - 1][c - 1] + \
                dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
        # 가로, 세로 파이프 추가
        if board[r][c] == 0:
            dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
            dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

print(sum(dp[i][N - 1][N - 1] for i in range(3)))
