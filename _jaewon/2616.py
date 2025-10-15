N = int(input())
people = list(map(int, input().split()))
people.insert(0, 0)

standard = int(input())

dp = [[0] * (N + 1) for _ in range(4)]

prefix_sum = [0]
for i in range(1, N + 1):
    prefix_sum.append(prefix_sum[i - 1] + people[i])

for i in range(1, 4):
    for j in range(standard, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - standard] + prefix_sum[j] - prefix_sum[j - standard])

print(dp[3][N])