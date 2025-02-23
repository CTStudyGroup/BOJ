N = int(input())

# dp: 전체 가져간 돌의 개수
dp = [0]*(N+1)

if N == 1 or N == 3 or N == 4:
    print("SK")
    exit()
if N == 2:
    print("CY")
    exit()

dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"
dp[4] = "SK"

for i in range(5, N+1):
    if dp[i-1] == "CY" or dp[i-3] == "CY" or dp[i-4] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"
print(dp[N])
