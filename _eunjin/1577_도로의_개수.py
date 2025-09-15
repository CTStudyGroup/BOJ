import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [[[0, [True, True]] for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1

K = int(sys.stdin.readline())
for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a > c:
        a, c = c, a
    if b > d:
        b, d = d, b
    d = 0 if c - a > d - b else 1
    dp[a][b][1][d] = False

moves = [(1, 0), (0, 1)]
for x in range(N + 1):
    for y in range(M + 1):
        for i in range(2):
            nx, ny = x + moves[i][0], y + moves[i][1]
            if nx <= N and ny <= M and dp[x][y][1][i]:
                dp[nx][ny][0] += dp[x][y][0]

print(dp[N][M][0])
