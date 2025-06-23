N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]

# A를 기준으로 전깃줄 정렬
line.sort(key=lambda x: x[0])

# 정렬 후 B는 [8,2,9,1,4,6,7,10]
# 여기서 LIS 길이를 구하면 전깃줄이 교차하지 않는 최대 길이 구할 수 있음

cnt = 0
dp = [1] * N
for i in range(N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
    cnt = max(cnt, dp[i])

print(N - cnt)
