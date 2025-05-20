N = input().strip()
MOD = 1000000

if N == '0':
    print(0)
    exit()

# 1~26까지 숫자 등장 시 경우의 수 +1
# dp
# 0으로 초기화 하고 바로 이전 자리 보면서 26이하이면 경우의수 +1

L = len(N)
dp = [0] * (L + 1)
dp[0] = 1

for i in range(L):
    if N[i] == '0':
        continue
    if i < L - 1 and '10' <= N[i:i + 2] <= '26':
        dp[i + 2] = (dp[i + 2] + dp[i]) % MOD
    dp[i + 1] = (dp[i + 1] + dp[i]) % MOD

print(dp[-1])
