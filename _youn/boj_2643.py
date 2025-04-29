def solve(N, papers):
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if papers[j][0] <= papers[i][0] and papers[j][1] <= papers[i][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return(max(dp))

N = int(input())
papers = []
for _ in range(N):
    n = tuple(map(int, input().split()))
    papers.append((min(n), max(n)))
print(solve(N, sorted(papers)))