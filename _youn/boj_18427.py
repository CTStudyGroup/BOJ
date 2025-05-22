N, M, H = map(int, input().split())
Blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1

for i, row in enumerate(Blocks):
    dp[i+1] = dp[i][:]
    for b in row:
        for h in range(b, H+1):
            dp[i+1][h] += dp[i][h - b] % 10007

print(dp[N][H] % 10007)