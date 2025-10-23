W, H = map(int, input().split())
MOD = 100000

# dp[x][y][dir][turn]
# dir: 0 = 동, 1 = 북
# turn: 0 = 방향 유지, 1 = 방금 방향을 바꾼 상태
dp = [[[[0] * 2 for _ in range(2)] for _ in range(H + 1)] for _ in range(W + 1)]

# 동쪽으로만 이동
for x in range(2, W + 1):
    dp[x][1][0][0] = 1

# 북쪽으로만 이동
for y in range(2, H + 1):
    dp[1][y][1][0] = 1

# DP 점화식
for x in range(2, W + 1):
    for y in range(2, H + 1):
        # 오른쪽으로 이동
        dp[x][y][0][0] = (dp[x - 1][y][0][0] + dp[x - 1][y][0][1]) % MOD  # 방향 유지
        dp[x][y][0][1] = dp[x - 1][y][1][0] % MOD  # 북 -> 동 전환

        # 위쪽으로 이동
        dp[x][y][1][0] = (dp[x][y - 1][1][0] + dp[x][y - 1][1][1]) % MOD  # 방향 유지
        dp[x][y][1][1] = dp[x][y - 1][0][0] % MOD  # 동 -> 북 전환

answer = (dp[W][H][0][0] + dp[W][H][0][1] + dp[W][H][1][0] + dp[W][H][1][1]) % MOD
print(answer)
