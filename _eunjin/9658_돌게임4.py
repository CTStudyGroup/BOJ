N = int(input())

if N == 1:
    print("CY")
    exit()
elif N == 2:
    print("SK")
    exit()
elif N == 3:
    print("CY")
    exit()
elif N == 4:
    print("SK")
    exit()

# dp??
dp = [0] * N
dp[0] = "CY"
dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"

for i in range(4, N):
    v1, v3, v4 = dp[i - 1], dp[i - 3], dp[i - 4]
    if v1 == "CY" or v3 == "CY" or v4 == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"

print(dp[-1])
