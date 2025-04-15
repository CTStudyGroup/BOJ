import sys
input = sys.stdin.readline

T = int(input())

# dp
# dp[a][b]: a자리의 마지막 숫자가 b일 때 가능한 답의 개수
# dp[y][x] = sum(dp[y-1][:x+1])
for _ in range(T):
    N = int(input())
    if N == 1:
        print(10)
        continue
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for y in range(2, N + 1):
        for x in range(10):
            dp[y][x] = sum(dp[y - 1][:x + 1])
    print(sum(dp[N]))
