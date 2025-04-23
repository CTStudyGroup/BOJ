import sys
input = sys.stdin.readline

# dp 배낭문제
# 최대 공부시간을 넘지 않으면서 중요도의 합이 최대가 되도록 과목을 담는 문제
N, K = map(int, input().split())
score = [0]
time = [0]
for _ in range(K):
    i, t = map(int, input().split())
    score.append(i)
    time.append(t)

# dp[i]][j]: i번째 과목까지 고려했을 때, 공부 시간을 j까지 사용했을 때 얻을 수 있는 최대 중요도
dp = [[0] * (N + 1) for _ in range(K + 1)]

# dp[i][j] = dp[i-1][j-time[i]] + score[i] , dp[i-1][j]
for i in range(1, K + 1):
    for j in range(1, N + 1):
        if time[i] <= j:
            dp[i][j] = max(dp[i - 1][j - time[i]] + score[i], dp[i - 1][j])  # i번째 과목을 선택 하는 경우, i번째 과목을 선택 안하는 경우
        else:
            dp[i][j] = dp[i - 1][j]  # i번째 과목을 선택 안하는 경우

print(dp[K][N])
