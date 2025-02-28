N = int(input())

arr = list(map(int, input().split()))

if N == 1:
    print(arr[0])
    exit()

# 수를 삭제 했는지 여부도 같이 저장해야된다
# dp[x][0] = x번째까지 수열에서 수를 제거하지 않은 경우 최대 연속합
# dp[x][0] = x번째까지 수열에서 수를 제거한 경우 최대 연속합

INF = -1e8

dp = [[INF, INF] for _ in range(N)]

dp[0][0] = arr[0]
dp[1][0] = max(arr[0] + arr[1], arr[1])
dp[1][1] = max(arr[0], arr[1])
# print(dp)

# dp[x][0] = x-1번째까지 제거 안한 합 + x번째, x번째만
# dp[x][1] = x-1번째까지 제거 안한 합, x-1번째까지 제거한 합 + x번째

for i in range(2, N):
    dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])

# print(dp)

mx = INF
for a, b in dp:
    mx = max(mx, a, b)

print(mx)
