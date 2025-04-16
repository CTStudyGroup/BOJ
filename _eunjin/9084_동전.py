T = int(input())

# 1원~N원까지 주어진 동전으로 만드는 경우의 수 계산 해나가기, 1원 계산 결과 -> 2원 계산 과정에 사용 가능
# dp

for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    target = int(input())

    # dp[y][x]: x번째 동전까지 사용을 고려해서 y원을 만드는 경우의 수
    dp = [[0] * (N + 1) for _ in range(target + 1)]

    # dp[y][x] = dp[y][x-1] + dp[y-coins[x]][x]

    for y in range(1, target + 1):
        for x in range(1, N + 1):
            if coins[x] == y:
                dp[y][x] = dp[y][x - 1] + 1
            elif coins[x] < y:
                dp[y][x] = dp[y][x - 1]
                dp[y][x] += dp[y - coins[x]][x]

    print(dp[target][N])

