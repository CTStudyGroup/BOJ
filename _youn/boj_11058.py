def solve(N):
    dp = [i for i in range(N+1)]

    for idx in range(7, N+1):
        dp[idx] = max(dp[idx-3]*2, dp[idx-4]*3, dp[idx-5]*4)
    return dp[N]

N = int(input())
print(solve(N))