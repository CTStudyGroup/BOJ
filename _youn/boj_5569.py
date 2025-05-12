def init(dp, w, h):
    for i in range(w):
        dp[i][0][1] = 1
    for j in range(h):
        dp[0][j][3] = 1
    return dp

def solve(dp, w, h):
    dp = init(dp, w, h)
    for i in range(1, w):
        for j in range(1, h):
            dp[i][j][0] = dp[i-1][j][3]
            dp[i][j][1] = (dp[i-1][j][0] + dp[i-1][j][1])%100000
            dp[i][j][2] = dp[i][j-1][1]
            dp[i][j][3] = (dp[i][j-1][2] + dp[i][j-1][3])%100000
    return sum(dp[w-1][h-1])%100000

w, h = map(int, input().split())
dp = [[[0]*4 for _ in range(h)] for _ in range(w)]
print(solve(dp, w, h))

