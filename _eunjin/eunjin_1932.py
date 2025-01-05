N = int(input())
triangle = []
for i in range(N):
    input_arr = list(map(int, input().split()))
    triangle.append(input_arr)


# print(triangle)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = triangle[0][0]

for n in range(1, N):
    for i in range(n+1):
        if(i-1 >= 0):
            dp[n][i] = max(dp[n-1][i-1], dp[n-1][i]) + triangle[n][i]
        else:
            dp[n][i] = dp[n-1][i] + triangle[n][i]

print(max(dp[N-1]))
