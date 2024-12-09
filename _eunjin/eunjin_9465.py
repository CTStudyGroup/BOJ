import sys
input = sys.stdin.readline

# 입력 받기
T = int(input())

for _ in range(T):
    N = int(input())

    sticker = [[0]+list(map(int, input().split())),
               [0]+list(map(int, input().split()))]

    # dp[y][x]: x번쨰 위치에서 y행의 스티커를 선택했을 때 스티커 점수의 최댓값
    dp = [[0 for _ in range(N+1)], [0 for _ in range(N+1)]]

    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]

    for i in range(2, N+1):
        dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2])+sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2])+sticker[1][i]

    # print("dp:", dp)
    print(max(dp[0][N], dp[1][N]))
