while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0:
        break

    board = [N * [0] for _ in range(M)]
    for y in range(M):
        board[y] = list(map(int, input().split()))

    total_row = [0] * M
    for y in range(M):
        max_row = [0] * N
        max_row[0] = board[y][0]
        if N >= 2:
            max_row[1] = max(board[y][0], board[y][1])
        for x in range(2, N):
            max_row[x] = max(max_row[x - 1], board[y][x] + max_row[x - 2])
        total_row[y] = max_row[N - 1]

    answer_dp = [0] * M
    answer_dp[0] = total_row[0]
    if M >= 2:
        answer_dp[1] = max(total_row[0], total_row[1])
    for y in range(2, M):
        answer_dp[y] = max(answer_dp[y - 1], total_row[y] + answer_dp[y - 2])

    print(answer_dp[M - 1])
