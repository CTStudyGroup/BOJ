N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# dp로 풀어야 한다
# dp[y][x]: (y,x)까지 탐색했을 때의 최대 자원 숫자
dp = [[0] * M for _ in range(N)]

dp[0][0] = matrix[0][0]

# 첫번째 행 초기화
for x in range(1, M):
    dp[0][x] = dp[0][x - 1] + matrix[0][x]

# 첫번째 열 초기화
for y in range(1, N):
    dp[y][0] = dp[y - 1][0] + matrix[y][0]

for y in range(1, N):
    for x in range(1, M):
        dp[y][x] = max(dp[y - 1][x], dp[y][x - 1]) + matrix[y][x]

print(dp[N - 1][M - 1])
