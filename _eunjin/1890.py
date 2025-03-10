N = int(input())
board = [input().split() for _ in range(N)]
M = len(board[0])

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(M):
        k = int(board[i][j])
        # 이동 가능한 거리가 0이라면 넘어간다.
        # 또는 dp가 0이라는 것은 현재 위치에 도달할 수 없음을 의미함으로 넘어간다.
        if k == 0 or dp[i][j] == 0:
            continue
        if i + k < N:  # 아래쪽으로 이동하는 경우, 게임판을 벗어나지 않는다면 경우의 수 추가
            dp[i + k][j] += dp[i][j]
        if j + k < M:  # 오른쪽으로 이동하는 경우, 게임판을 벗어나지 않는다면 경우의 수 추가
            dp[i][j + k] += dp[i][j]

print(dp[-1][-1])
