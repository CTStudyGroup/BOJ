def solve(N):
    dp = [False for _ in range(N+1)] # SK win -> True
    dp[2] = True 
    for i in range(4, N+1):
        if dp[i-1] and dp[i-3] and dp[i-4]: continue
        else: dp[i] = True
    return 'SK' if dp[N] else 'CY'

N = int(input())
print(solve(N))
