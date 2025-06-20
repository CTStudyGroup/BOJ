from collections import defaultdict

def valid(idx):
    global banned
    return not (idx in banned)

def solve(N, banned):
    dp = defaultdict(dict)
    dp[2][1] = 1

    for i in range(2, N+1):
        if i in banned or i not in dp: continue

        for j in dp[i]:
            for nj in [j-1, j, j+1]:
                if nj <=0: continue
                ni = i + nj
                if ni in banned or ni > N: continue
                if nj not in dp[ni] or dp[ni][nj] > dp[i][j] + 1:
                    dp[ni][nj] = dp[i][j] + 1
    return min(dp[N].values()) if N in dp else -1

N, M = map(int, input().split())
banned = [int(input()) for _ in range(M)]
print(solve(N, set(banned)))