def solve(N, children):
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if children[j]<children[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return N-max(dp)

N = int(input())
children = []
for _ in range(N):
    children.append(int(input()))
print(solve(N, children))