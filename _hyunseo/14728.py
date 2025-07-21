N, T = map(int, input().split())
study_units = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (T + 1)

for time, score in study_units:
    for t in range(T, time - 1, -1):  # 뒤에서부터 탐색
        dp[t] = max(dp[t], dp[t - time] + score)

print(dp[T])
