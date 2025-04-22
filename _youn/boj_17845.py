def getMax(subjects, N):
    dp = [[0]*(N+1) for _ in range(len(subjects)+1)]
    for i, (im, w) in enumerate(subjects):
        dp[i+1] = dp[i][:w] + [0]*(N-w+1)
        for j in range(w, N+1):
            dp[i+1][j] = max(dp[i][j], dp[i][j-w]+im)
    return dp[-1][N]

N, K = list(map(int, input().split()))
subjects = [list(map(int, input().split())) for _ in range(K)]
print(getMax(subjects, N))