def solve(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for h in range(n+1): 
        for w in range(n+1):
            if w < h: continue
            if h == 0: dp[w][h] = 1
            else: dp[w][h] = dp[w][h-1] + dp[w-1][h]
    return dp

dp = solve(30)
while True:
    n = int(input())
    if n == 0: break
    print(dp[n][n])