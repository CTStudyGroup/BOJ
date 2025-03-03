N, M = map(int, input().split())

vacations = []
if M > 0:
    vacations = list(map(int, input().split()))

INF = float('inf')

# dp[a][b]: a일까지, 남은 쿠폰 개수가 b개 일때 비용의 최솟값
dp = [[INF] * 42 for _ in range(106)]
dp[0][0] = 0

for i in range(N + 1):
    for j in range(40):
        if dp[i][j] == float('inf'):
            continue

        # 내일 날짜가 방문 불가한 날인 경우
        if i + 1 in vacations:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])

        # 쿠폰 사용 가능한 경우
        if j >= 3:
            dp[i + 1][j - 3] = min(dp[i][j], dp[i + 1][j - 3])

        # 1일권 구매하는 경우
        dp[i + 1][j] = min(dp[i][j] + 10000, dp[i + 1][j])

        # 3일권 구매하는 경우
        for k in range(1, 4):
            dp[i + k][j + 1] = min(dp[i][j] + 25000, dp[i + k][j + 1])

        # 5일권 구매하는 경우
        for k in range(1, 6):
            dp[i + k][j + 2] = min(dp[i][j] + 37000, dp[i + k][j + 2])

# print(dp)
print(min(dp[N]))
