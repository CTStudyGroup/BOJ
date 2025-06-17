import sys
input = sys.stdin.readline

# dp 배낭문제
# unbounded knapsack

while True:
    N, M = input().split()
    N = int(N)
    M = int(round(float(M) * 100))

    if N == 0 and M == 0.00:
        exit()

    pr = []
    kcal = []

    for _ in range(N):
        c, p = input().split()
        c = int(c)
        p = int(round(float(p) * 100))
        kcal.append(c)
        pr.append(p)

    dp = [0] * (M + 1)
    for i in range(N):
        for j in range(pr[i], M + 1):
            dp[j] = max(dp[j], dp[j - pr[i]] + kcal[i])

    print(dp[M])
