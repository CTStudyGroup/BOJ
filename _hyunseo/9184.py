dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if min(a, b, c) <= 0:
        return 1
    if  max(a,b,c) > 20:
        return w(20, 20, 20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print(f"w({x}, {y}, {z}) = {w(x, y, z)}")
