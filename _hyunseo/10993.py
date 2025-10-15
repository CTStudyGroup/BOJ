
def make_outer_start(n, m) :
    """n이 세로, m이 가로"""
    board = [[' ']*m for _ in range(n)]
    center = m//2
    board[0][center] = "*"
    for i in range(1, n-1) :
        board[i][center-i] = "*"
        board[i][center+i] = "*"
    for i in range(m) :
        board[n-1][i] = "*"
    return board
def join_stars(board, little_start, s_start, g_start) :
    for s in range(s_start, s_start + len(little_start)) :
        for g in range(g_start, g_start + len(little_start[0])) :
            board[s][g] = little_start[s- s_start][g- g_start]
    return board

def solve() :
    dp = []
    dp.append(0)
    dp.append(["*"])
    a, b = 1, 1
    for t in range(2, N) :
        a, b = a*2 + 1, b*2 + 3
        board = make_outer_start(a, b)
        if t % 2 == 0:   # 짝수면 뒤집기
            board = board[::-1]

        small_h = len(dp[t-1])
        small_w = len(dp[t-1][0])

        if t % 2 == 1:  # 홀수 단계 (upright)
            s_start = a - small_h -1
            g_start = (b - small_w) // 2
        else:           # 짝수 단계 (upside-down)
            s_start = 1
            g_start = (b - small_w) // 2

        dp.append(join_stars(board, dp[t-1], s_start, g_start))
    # for star in dp[1:] :
    #     for line in star :
    #         print(*line, sep = "")
    return dp[1:]
N = int(input()) + 1
if N == 1 :
    print("*")
    exit()
dp = solve()
for line in dp[-1] :
    print("".join(line).rstrip())
