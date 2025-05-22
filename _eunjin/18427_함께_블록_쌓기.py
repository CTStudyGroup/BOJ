import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = [0] + [list(map(int, input().split())) for _ in range(N)]
MOD = 10007

# dp[i][j]: i번째 사람까지 고려했을 때 j 높이를 만들 수 있는 경우의 수
dp = [[0] * (H + 1) for _ in range(N + 1)]

# 높이 0을 만드는 경우의 수 1
for i in range(N + 1):
    dp[i][0] = 1

for i in range(1, N + 1):
    for h in range(H + 1):
        dp[i][h] = dp[i - 1][h]

    for block in blocks[i]:
        for j in range(block, H + 1):
            dp[i][j] += dp[i - 1][j - block]

print(dp[N][H] % MOD)
