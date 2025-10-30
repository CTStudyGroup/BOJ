import sys
input = sys.stdin.readline
N = int(input())
INF = int(1e9)

matrix = [list(map(int, input().split())) for _ in range(N)]

# dp
# 버튼 안눌러도 되는 경우
# dp[y][x] = min(dp[y-1][x],dp[y][x-1])
# 버튼 눌러야 되는 경우
# dp[y][x] = dp[y-1][x] + 버튼 누르는 횟수
# dp[y][x] = dp[y][x-1] + 버튼 누르는 횟수

dp = [[INF] * N for _ in range(N)]
dp[0][0] = 0

# 0열 초기화
for y in range(1, N):
    diff = matrix[y][0] - matrix[y - 1][0]
    if diff >= 0:
        dp[y][0] = dp[y - 1][0] + diff + 1
    else:
        dp[y][0] = dp[y - 1][0]

# 0행 초기화
for x in range(1, N):
    diff = matrix[0][x] - matrix[0][x - 1]
    if diff >= 0:
        dp[0][x] = dp[0][x - 1] + diff + 1
    else:
        dp[0][x] = dp[0][x - 1]

for y in range(1, N):
    for x in range(1, N):
        # 위 방향
        diff = matrix[y][x] - matrix[y - 1][x]
        if diff >= 0:
            dp[y][x] = min(dp[y - 1][x] + diff + 1, dp[y][x])
        else:
            dp[y][x] = min(dp[y][x], dp[y - 1][x])

        # 왼쪽 방향
        diff = matrix[y][x] - matrix[y][x - 1]
        if diff >= 0:
            dp[y][x] = min(dp[y][x], dp[y][x - 1] + diff + 1)
        else:
            dp[y][x] = min(dp[y][x], dp[y][x - 1])

print(dp[N - 1][N - 1])
