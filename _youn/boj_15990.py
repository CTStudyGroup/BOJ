def solve(N):
    dp = [[0]*4 for _ in range(max(N)+1)]

    dp[1]=[0,1,0,0]
    dp[2]=[0,0,1,0]
    dp[3]=[0,1,1,1]
    
    for n in range(max(N)+1):
        if n < 4: continue
        dp[n][1] = (dp[n-1][2] + dp[n-1][3])%1000000009
        dp[n][2] = (dp[n-2][1] + dp[n-2][3])%1000000009
        dp[n][3] = (dp[n-3][1] + dp[n-3][2])%1000000009

    ans = []
    for n in N:
        ans.append(sum(dp[n])%1000000009)
    return ans

T = int(input())
N = [int(input()) for _ in range(T)]
print(*solve(N), sep='\n')    