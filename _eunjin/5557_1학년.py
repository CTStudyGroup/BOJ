N = int(input())
arr = list(map(int, input().split()))

# 백트래킹 = 시간초과
# dp로 해야한다
# dp[x][y]: x번째 숫자까지 사용했을 때, 식의 값이 y가 되는 경우의 수
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][arr[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[N - 2][arr[-1]])

